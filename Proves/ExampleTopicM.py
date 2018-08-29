import tweepy
auth = tweepy.OAuthHandler("Hdah781zeulKrfrMzK3iI6GTs", "tFLvGas5hrXwq4yiXheQj5On99VUoAl5Fpcl6vRQqatjxISFDZ")
auth.set_access_token("988457597241118720-NIGfC9gqlNakSIcmDZfVAvb5LZHDgqa", "SyoofoDP3GJsDhRFHdjjsIMAFLp2XwBYXakVyUhb3YvAE")

api = tweepy.API(auth)

print (api)

# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
#     print (status._json['text'])

tlist = []
it = 0
for tweet in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
    # Write a row to the CSV file. I use encode UTF-8
    # print (tweet.created_at, tweet.text)
    tlist.append(tweet.text)
    it = it+1
    if it > 50: 
        break

print (tlist)


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])

no_features = 10

# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(tlist)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
# import numpy as np
# from sklearn.decomposition import NMF
# model = NMF(n_components=2, init='random', random_state=0)
# W = model.fit_transform(tlist)
# H = model.components_

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(tlist)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 5

# Run NMF
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Run LDA
lda = LatentDirichletAllocation(n_components=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)