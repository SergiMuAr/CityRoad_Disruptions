from sklearn import svm
import csv
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split

class SVMmodel:
    def __init__(self):
        self._tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
        data = pd.read_csv('DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
        text = data['Text']
        target = data['Class']
        
        train_matrix = self._tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
        print (train_matrix.shape) # 445 tweets are represented by 387 features.

        # # splitting data into test and train
        # X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=0.3, random_state=None)
        # print (X_train.shape, y_train.shape)
        # print (X_test.shape, y_test.shape)
        self._clf = svm.SVC(kernel='linear', C=1).fit(train_matrix, target)
        # score2 = self._clf.score(X_test, y_test)
        # print (score2)
        
        # data_test = pd.read_csv('Proves/JocsDeProves/testBO.csv', sep = '\t', lineterminator='\n')
        # test_text = data_test['Text']
        # test_class = data_test['Class']
        # test_matrix = self._tf_vectorizer.transform(test_text).toarray()
        # predict2 = self._clf.predict(test_matrix)
        # print (predict2)

    
    def predictText(self,text):
        text_test = self._tf_vectorizer.transform([text]).toarray()
        # print(self._clf.predict(text_test))
        return self._clf.predict(text_test)[0]