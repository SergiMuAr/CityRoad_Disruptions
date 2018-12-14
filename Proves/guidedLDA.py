import numpy as np
import guidedlda
import csv

tlist = []
with open('TrainingDataSet/stemmed2.csv') as f:
  reader = csv.reader(f)

  for row in reader:
        tlist.append(','.join(row))

          
print (tlist[0])
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=100)
X = tf_vectorizer.fit_transform(tlist)
vocab = tf_vectorizer.get_feature_names()


# X = guidedlda.datasets.load_data(guidedlda.datasets.NYT)
# vocab = guidedlda.datasets.load_vocab(guidedlda.datasets.NYT)
word2id = dict((v, idx) for idx, v in enumerate(vocab))

print(X.shape)

print(X.sum())
# # Normal LDA without seeding
# model = guidedlda.GuidedLDA(n_topics=2, n_iter=10000, random_state=7, refresh=20)
# model.fit(X)

# topic_word = model.topic_word_
# n_top_words = 8
# for i, topic_dist in enumerate(topic_word):
#     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
#     print('Topic {}: {}'.format(i, ' '.join(topic_words)))


# Guided LDA with seed topics.
seed_topic_list = [['accident', 'retencions', 'cues', 'tallat', 'obres', 'ap7', 'b30'],
                   []]

model = guidedlda.GuidedLDA(n_topics=2, n_iter=1000, random_state=7, refresh=20)

seed_topics = {}
for t_id, st in enumerate(seed_topic_list):
    for word in st:
        seed_topics[word2id[word]] = t_id

model.fit(X, seed_topics=seed_topics, seed_confidence=0.15)

n_top_words = 10
topic_word = model.topic_word_
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

# Provar tweets
with open('JocsDeProves/testDataSet.csv') as f:
        reader = csv.reader(f)
        i = 1
        for row in reader:
                text = ','.join(row)
                x = model.transform(tf_vectorizer.transform([text]))[0]
                print ("Pel text ", i,", LDA es: ", x)
                i = i+1
