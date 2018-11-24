import csv

tlist = []
with open('TrainingDataSet/stemmed2.csv') as f:
  reader = csv.reader(f)

  for row in reader:
        tlist.append(','.join(row))

          
print (tlist[0])

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic:")
        print (topic_idx)
        print (" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

no_features = 100


# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(tlist)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 3

# Run LDA
lda = LatentDirichletAllocation(n_components=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

no_top_words = 10
# display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)



# text = "S'han detectat interrupcions degut a incidencies. Accident a Torredembarra."

# # LDA
# x = lda.transform(tf_vectorizer.transform([text]))[0]
# print ("Pel primer text, LDA es: ", x )

# text2 = "Exemple dun tweet que no te res a veure amb el tema i espero que no generi correlacions amb topics entrenats."

# # LDA
# x = lda.transform(tf_vectorizer.transform([text2]))[0]
# print ("Pel segon text, LDA es: ", x)

# text3 = "pluja seguretat distància velocitat augmenta recorda consel carretera inuncat vehicl 15 aigua protecciocivil precaució modera prudència meteocat transit intensitat visibilitat"
# x = lda.transform(tf_vectorizer.transform([text3]))[0]
# print ("Pel tercer text, LDA es: ", x)

with open('JocsDeProves/testDataSet.csv') as f:
        reader = csv.reader(f)
        i = 1
        for row in reader:
                text = ','.join(row)
                x = lda.transform(tf_vectorizer.transform([text]))[0]
                print ("Pel text ", i,", LDA es: ", x)
                i = i+1


# Crec que està fallant perque no està agafant bé el text a vectoritzar -> [text][0]



# # Implementing similarities
# from sklearn.metrics.pairwise import euclidean_distances
# def most_similar(x, Z, top_n=5):
# dists = euclidean_distances(x.reshape(1, -1), Z)
# pairs = enumerate(dists[0])
# most_similar = sorted(pairs, key=lambda item: item[1])[:top_n]
# return most_similar
# similarities = most_similar(x, nmf_Z)
# document_id, similarity = similarities[0]
# print(data[document_id][:1000])
