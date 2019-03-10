from sklearn import svm
import csv
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split

class SVMmodel:
    _tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
    def trainModel():
        data = pd.read_csv('DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
        text = data['Text']
        target = data['Class']
        
        data_test = pd.read_csv('Proves/JocsDeProves/testBO.csv', sep = '\t', lineterminator='\n')
        test_text = data_test['Text']
        test_class = data_test['Class']
        
        train_matrix = _tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
        test_matrix = _tf_vectorizer.transform(test_text).toarray()
        print (train_matrix.shape) # 445 tweets are represented by 387 features.

        # splitting data into test and train
        X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=0.01, random_state=0)
        print (X_train.shape, y_train.shape)
        print (X_test.shape, y_test.shape)
        # X_train = tf_vectorizer.fit_transform(X_train.values.astype('U')).toarray()
        _clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
        score2 = _clf.score  (X_test, y_test)
        print (score2)
        predict2 = _clf.predict(test_matrix)
        print (predict2)

    
    def predictText(text):
        text_test = _tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
        print(_clf.predict(text_test))