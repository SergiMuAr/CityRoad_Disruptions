import csv
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split

tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
data = pd.read_csv('../DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
text = data['Text']
target = data['Class']
train_matrix = tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
print (train_matrix.shape) # 445 tweets are represented by 387 features.
tf_feature_names = tf_vectorizer.get_feature_names()
# X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=0.3, random_state=None)

from sklearn.decomposition import TruncatedSVD

# SVD represent documents and terms in vectors 
svd_model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, random_state=122)

svd_model.fit(train_matrix)

len(svd_model.components_)

terms = tf_vectorizer.get_feature_names()

for i, comp in enumerate(svd_model.components_):
    terms_comp = zip(terms, comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
    print("Topic "+str(i)+": ")
    for t in sorted_terms:
        print(t[0])