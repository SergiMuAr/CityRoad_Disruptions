from sklearn.ensemble import GradientBoostingClassifier
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
# Parameters= {'gboost__criterion': 'friedman_mse', 'gboost__learning_rate': 0.4, 'gboost__loss': 'deviance', 'gboost__max_depth': 9, 'gboost__max_features': 'log2', 'gboost__min_samples_leaf': 3, 'gboost__min_samples_split': 6, 'gboost__n_estimators': 180, 'gboost__subsample': 0.9}
clf = GradientBoostingClassifier(criterion= 'friedman_mse', learning_rate= 0.4, loss= 'deviance', max_depth=9, max_features='log2', min_samples_leaf=3, min_samples_split=6, n_estimators=180, subsample=0.9).fit(X_train, y_train)
score = clf.score  (X_test, y_test)
print (score)

