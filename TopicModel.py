from sklearn import svm
import csv
import numpy as np
import pandas as pd


# test_text = []
# with open('JocsDeProves/testBO.csv') as f:
#   reader = csv.reader(f)
#   for row in reader:
#         test_text.append(','.join(row))

# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
# train_matrix = tf_vectorizer.fit_transform(text).toarray()
# test_matrix = tf_vectorizer.transform(test_text).toarray()

# from sklearn.feature_selection import chi2
# print (train_matrix.shape) # 445 tweets are represented by 387 features.

# model = svm.SVC(kernel='linear', gamma=1) 
# # there is various option associated with it, like changing kernel, gamma and C value. Will discuss more # about it in next section.Train the model using the training sets and check score
# model.fit(train_matrix, target)
# print (model.score(train_matrix, target))
# print (model.predict(test_matrix))

def trainModel(trainingDF):
    data = pd.read_csv(trainingDF, sep = '\t', lineterminator='\n')
    text = data['Text']
    target = data['Class']
    print ()