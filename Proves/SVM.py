#Import Library
from sklearn import svm
import csv
import numpy as np
import pandas as pd

data = pd.read_csv('TrainingDataSet/trainingBO.csv', sep = '\t', lineterminator='\n')
text = data['Text'] #you can also use df['column_name']
target = data['Class']

# data_test = pd.read_csv('JocsDeProves/testBO.csv',  sep = '\t', lineterminator='\n')
# test_text = data_test['Text']
# test_target = data_test['Class']

test_text = []
with open('TrainingDataSet/stemmedNTI.csv') as f:
  reader = csv.reader(f)
  for row in reader:
        test_text.append(','.join(row))



#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object 

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# tf_vectorizer = CountVectorizer(max_df=0.95, min_df=5, max_features=100)
# tf = tf_vectorizer.fit_transform(tlist)
# tf_feature_names = tf_vectorizer.get_feature_names()

# print ("FEATURES")
# print (tf)
# print (tf_feature_names)

tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
train_matrix = tf_vectorizer.fit_transform(text).toarray()
test_matrix = tf_vectorizer.transform(test_text).toarray()

# labels = df.category_id

from sklearn.feature_selection import chi2
print (train_matrix.shape) # 445 tweets are represented by 387 features.

model = svm.SVC(kernel='linear', gamma=1) 
# there is various option associated with it, like changing kernel, gamma and C value. Will discuss more # about it in next section.Train the model using the training sets and check score
model.fit(train_matrix, target)
print (model.score(train_matrix, target))
print (model.predict(test_matrix))