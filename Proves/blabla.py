from sklearn import svm
import csv
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split


tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=20, norm='l2', encoding='latin-1', ngram_range=(1, 2))
data = pd.read_csv('../DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
df = data.loc[:300]

    
text = df['Text']
target = df['Class']
train_matrix = tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
tf_feature_names = tf_vectorizer.get_feature_names()
print (tf_feature_names)
