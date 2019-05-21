import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os

import scipy.stats as st
from scipy.stats import randint as sp_randint

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score, RandomizedSearchCV


pd.set_option('display.max_columns', None) # Display all cols in describe
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def get_classifiers(labels):

    models = {
        'knn': KNeighborsClassifier(),
        'svm': SVC(cache_size=900),
        'rf': RandomForestClassifier(),
        'neural': MLPClassifier()
    }

    params = {
        'knn': dict(n_neighbors=list(range(1, 30 + 1, 2))),
        'svm': dict(C=[1e-3, 1e-2, 1e-1, 1, 10, 100],
               kernel=['linear', 'rbf', 'sigmoid', 'poly'],
               degree=[2, 3],
               gamma=['auto', 'scale'],
               shrinking=[True, False],
               tol=[1e-1, 1e-3, 1e-5]),
        'rf': dict(n_estimators=list(range(10, 150 + 1, 10)),
               criterion=['gini', 'entropy'],
               max_depth=[None] + list(range(5, 20 + 1, 5)),
               min_samples_split=sp_randint(2, 8),
               min_samples_leaf=sp_randint(1, 8),
               max_features=[None, 'sqrt', 'log2', 0.9, 0.85, 0.75],
               bootstrap=[True, False]),
        'neural': dict(hidden_layer_sizes=[(100, ), (100, 100, ), (100, 100, 100, )],
                activation=['identity', 'logistic', 'tanh', 'relu'],
                solver=['lbfgs', 'sgd', 'adam'],
                alpha=[1, 1e-1, 1e-2, 1e-4],
                learning_rate=['constant', 'invscaling', 'adaptive'],
                learning_rate_init=[1e-1, 1e-3, 1e-5])
    }

    classifiers = []
    params_list = []
    for label in labels:
        param = params[label]
        clf = models[label]

        new_keys = {}
        for key in param.keys():
            new_keys[key] = label + '__' + key

        for old, new in new_keys.items():
            param[new] = param.pop(old)

        classifiers.append((label, clf))
        params_list.append(param)

    return classifiers, params_list

def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                results['mean_test_score'][candidate],
                results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")


def randomized_search(pipe, params, n_iter, n_cv, X_train, y_train, scorer):
    random_search = RandomizedSearchCV(estimator=pipe, param_distributions=params, n_iter=n_iter, cv=n_cv,
                                       scoring=scorer, verbose=True, n_jobs=-1)
    start = time.time()
    random_search.fit(X_train, y_train)
    print(f'RandomizedSearchCV took {time.time() - start:.2f} seconds for {n_iter} candidates parameter settings.')
    report(random_search.cv_results_)
    return random_search


def parameter_fine_tuning(X_train, y_train, classifiers, params, n_iter, n_cv):
    scaler = ('scaler', StandardScaler())
    scorer = 'accuracy'

    best_params = {}
    for classifier, param in zip(classifiers, params):
        model = classifier[0]
        print('Training', model, 'model..')
        pipe = Pipeline([scaler, classifier])
        reg_search = randomized_search(pipe, param, n_iter, n_cv, X_train, y_train, scorer)
        best_params[model] = reg_search.best_params_

    return best_params


def test_predict(X_train, y_train, X_test, y_test, classifiers, best_params):

    for clf_name, clf in classifiers:
        print(clf_name)
        params = {}
        n_comp_pca = -1
        for param, value in best_params[clf_name].items():
            if param[:3] == 'pca': n_comp_pca = value; continue
            param = param.split('__')[1]
            #if value != None: params[param] = value
            params[param] = value

        clf = (clf_name, clf.set_params(**params))
        scaler = ('scaler', StandardScaler())
        pipe = Pipeline([scaler, clf])

        print('Training model..')
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)

        print(confusion_matrix(y_test, y_pred))
        print(f'Accuracy: {accuracy_score(y_test, y_pred) * 100 :.2f}')
        print(classification_report(y_test, y_pred))

        # print(f'f1-score pos: {f1_score(y_test, y_pred, pos_label=1) :.3f}')
        # print(f'f1-score neg: {f1_score(y_test, y_pred, pos_label=0) :.3f}' + '\n')
        # print(
        #     f'f1-score binary (pos): {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="binary") :.3f}')
        # print(f'f1-score micro: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="micro") :.3f}')
        # print(f'f1-score macro: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="macro") :.3f}')
        # print(f'f1-score weighted: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="weighted") :.3f}' + '\n\n')
        # print(f'f1-score: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="binary")}')

        # prediction = pd.DataFrame( {'customerID': test.customerID, 'Churn': y_pred} )
        # prediction.to_csv('./predictions/' + label + '_prediction.csv', index=False)


if __name__ == '__main__':
    n_iter = 50
    n_cv = 7

    data = pd.read_csv('/home/sergi/CityRoad_Disruptions/DataSet/preprocessed.csv', sep='\t',
                       lineterminator='\n')
    text = data['Text']
    target = data['Class']

    tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
    train_matrix = tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
    X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=.3)

    models = ['knn', 'lr', 'svm', 'dt', 'rf', 'gboost', 'neural']
    classifiers, params = get_classifiers(models)
    best_params = parameter_fine_tuning(X_train, y_train, classifiers, params, n_iter, n_cv)
    test_predict(X_train, y_train, X_test, y_test, classifiers, best_params)
