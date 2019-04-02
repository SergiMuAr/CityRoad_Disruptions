#Import Library
import numpy as np
from sklearn import svm
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split

data = pd.read_csv('TrainingDataSet/preprocessedDS.csv', sep = '\t', lineterminator='\n')
text = data['Text']
# print (text)
target = data['Class']


data = pd.read_csv('JocsDeProves/testBO.csv', sep = '\t', lineterminator='\n')
test_text = data['Text']
# print (text)
test_class = data['Class']

# data_test = pd.read_csv('JocsDeProves/testBO.csv',  sep = '\t', lineterminator='\n')
# test_text = data_test['Text']
# test_target = data_test['Class']

# test_text = []
# with open('JocsDeProves/testPreprocess.csv') as f:
#   reader = csv.reader(f)
#   for row in reader:
#         test_text.append(','.join(row))

# def plot_coefficients(classifier, feature_names, top_features=20):
#  coef = classifier.coef_.ravel()
#  top_positive_coefficients = np.argsort(coef)[-top_features:]
#  top_negative_coefficients = np.argsort(coef)[:top_features]
#  top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
#  # create plot
#  plt.figure(figsize=(15, 5))
#  colors = [‘red’ if c < 0 else ‘blue’ for c in coef[top_coefficients]]
#  plt.bar(np.arange(2 * top_features), coef[top_coefficients], color=colors)
#  feature_names = np.array(feature_names)
#  plt.xticks(np.arange(1, 1 + 2 * top_features), feature_names[top_coefficients], rotation=60, ha=’right’)
#  plt.show()

#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object 

# tf_vectorizer = CountVectorizer(max_df=0.95, min_df=5, max_features=100)
# tf = tf_vectorizer.fit_transform(tlist)
# tf_feature_names = tf_vectorizer.get_feature_names()

# print ("FEATURES")
# print (tf)
# print (tf_feature_names)

tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
train_matrix = tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
test_matrix = tf_vectorizer.transform(test_text).toarray()
tweet = "heeeelooou estic parlant de qualssevol parida que no és el tema"
test_tweet = tf_vectorizer.transform([tweet]).toarray()
print (train_matrix.shape) # 445 tweets are represented by 387 features.

# from sklearn.decomposition import PCA
# pca = PCA(n_components=2).fit(train_matrix)
# print (pca.explained_variance_ratio_)
# data2D = pca.transform(train_matrix)
# plt.scatter(data2D[:,0], data2D[:,1], c=target)
# plt.show()

# labels = df.category_id

from sklearn.feature_selection import chi2

model = svm.SVC(probability=True, kernel='linear')
# there is various option associated with it, like changing kernel, gamma and C value. Will discuss more # about it in next section.Train the model using the training sets and check score
model.fit(train_matrix, target)
score = model.score(train_matrix, target)
print (score)
predict = model.predict(test_tweet)
print (predict)
# print (np.transpose(test_class))

# splitting data into test and train
X_train, X_test, y_train, y_test = train_test_split(train_matrix, target, test_size=0.01, random_state=None)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)
# X_train = tf_vectorizer.fit_transform(X_train.values.astype('U')).toarray()
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score2 = clf.score  (X_test, y_test)
print (score2)
predict2 = clf.predict(test_tweet)
print (predict2)
# plot_coefficients(model, cv.get_feature_names())


# print (train_matrix)
# X = train_matrix[:, :2] # we only take the first two features. We could
#  # avoid this ugly slicing by using a two-dim dataset
# y = target
# # we create an instance of SVM and fit out data. We do not scale our
# # data since we want to plot the support vectors
# C = 1.0 # SVM regularization parameter
# svc = svm.SVC(kernel='linear', C=1,gamma='auto').fit(X, y)

# print ("HOLA")

# # create a mesh to plot in
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# h = (x_max / x_min)/100

# print (x_min, x_max, y_min, y_max, h)
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#  np.arange(y_min, y_max, h))
# plt.subplot(1, 1, 1)
# Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.xlim(xx.min(), xx.max())
# plt.title('SVC with linear kernel')
# plt.show()


from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic:")
        print (topic_idx)
        print (" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

lda = LatentDirichletAllocation(n_components=2, max_iter=100, learning_method='online', learning_offset=50.,random_state=None).fit(train_matrix)
print("Log Likelihood: ", lda.score(train_matrix))
print(lda.get_params())
no_top_words = 15
# display_topics(nmf, tfidf_feature_names, no_top_words)
tf_feature_names = tf_vectorizer.get_feature_names()
display_topics(lda, tf_feature_names, no_top_words)
