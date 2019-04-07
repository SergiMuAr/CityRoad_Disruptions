import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import csv
import pandas as pd
from sklearn.pipeline import Pipeline


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
data = pd.read_csv('DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
text = data['Text']
target = data['Class']

data_test = pd.read_csv('Proves/JocsDeProves/testBO.csv', sep = '\t', lineterminator='\n')
test_text = data_test['Text']
test_class = data_test['Class']

train_matrix = tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
test_matrix = tf_vectorizer.transform(test_text).toarray()
# print (train_matrix.shape) # 445 tweets are represented by 387 features.

# splitting data into test and train
X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=0.01, random_state=0)

classifiers = [
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

names = ["Linear SVM", "RBF SVM", "Gaussian Process",
        "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
        "Naive Bayes", "QDA"]


# Scoring and metrics
scaler = ('scaler', StandardScaler())
for clf, label in zip(names, classifiers):
    
    pipe = Pipeline([scaler, (label, clf)])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    
    print(label)
    print(confusion_matrix(y_test, y_pred))
    print(f'Accuracy: {accuracy_score(y_test, y_pred)*100 :.2f}')
    print(classification_report(y_test, y_pred))
    
    print(f'f1-score pos: {f1_score(y_test, y_pred, pos_label=1) :.3f}')
    print(f'f1-score neg: {f1_score(y_test, y_pred, pos_label=0) :.3f}' + '\n')
    print(f'f1-score binary (pos): {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="binary") :.3f}')
    print(f'f1-score micro: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="micro") :.3f}')
    print(f'f1-score macro: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="macro") :.3f}')
    print(f'f1-score weighted: {f1_score(y_test, y_pred, pos_label=1, labels=[1, 0], average="weighted") :.3f}' + '\n\n')


# # Cross validation
# for clf, label, pca_c in zipper:
#     #pca = ('pca', PCA(n_components=pca_c))
#     pipe = Pipeline([scaler, (label, clf)])
#     scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy', n_jobs=-1)
#     print("Accuracy: %0.3f (+/- %0.3f) [%s] <br>" % (scores.mean(), scores.std(), label))


# # Hyperparameter tuning with RandomizedSerach
# random_search = RandomizedSearchCV(estimator=pipe, param_distributions=params, n_iter=n_iter, cv=3,
#                                        scoring=scorer,
#                                        verbose=True, n_jobs=-1)
#     start = time.time()
#     random_search.fit(X_train, y_train)
#     print(f'RandomizedSearchCV took {time.time() - start:.2f} seconds for {n_iter} candidates parameter settings.')