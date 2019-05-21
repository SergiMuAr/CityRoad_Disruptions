from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split

data = pd.read_csv('/home/sergi/CityRoad_Disruptions/DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
text = data['Text']
target = data['Class']
tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
train_matrix = tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
tweet = "heeeelooou estic parlant de qualssevol parida que no és el tema"
test_tweet = tf_vectorizer.transform([tweet]).toarray()

X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=0.3, random_state=None)
# Parameters: {'neural__solver': 'adam', 'neural__learning_rate_init': 0.001, 'neural__learning_rate': 'constant', 'neural__hidden_layer_sizes': (100,), 'neural__alpha': 1, 'neural__activation': 'logistic'}
clf = MLPClassifier(solver='adam', learning_rate_init=0.001, learning_rate= 'constant', hidden_layer_sizes=(100,), alpha=1, activation='logistic').fit(X_train, y_train)
score = clf.score  (X_test, y_test)
print (score)

Parameters: {'gboost__criterion': 'mse', 'gboost__learning_rate': 0.2, 'gboost__loss': 'exponential', 'gboost__max_depth': 9, 'gboost__max_features': 'log2', 'gboost__min_samples_leaf': 3, 'gboost__min_samples_split': 6, 'gboost__n_estimators': 110, 'gboost__subsample': 0.75}
