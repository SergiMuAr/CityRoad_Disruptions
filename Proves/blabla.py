from arcgis.geocoding import geocode

results = geocode('New York St, Redlands, CA')
# query the first matched result
results[0]['location']

# from sklearn.datasets import fetch_20newsgroups
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.decomposition import PCA
# from sklearn.pipeline import Pipeline
# import matplotlib.pyplot as plt

# newsgroups_train = fetch_20newsgroups(subset='train', 
#                                       categories=['alt.atheism', 'sci.space'])
# pipeline = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
# ])        
# X = pipeline.fit_transform(newsgroups_train.data).todense()

# pca = PCA(n_components=2).fit(X)
# data2D = pca.transform(X)
# plt.scatter(data2D[:,0], data2D[:,1], c=data.target)
# plt.show()              #not required if using ipython notebook

# import nltk
# import csv
# import string
# import re
# from nltk.tokenize.toktok import ToktokTokenizer

# toktok = ToktokTokenizer()
# sent = u"¿Quién eres tú? ¡Hola! ¿Dónde estoy?"
# toktok.tokenize(sent)
# result = " ".join(toktok.tokenize(sent)) 
# print (result)

# from nltk import sent_tokenize
# sentences = u"¿Quién eres tú? ¡Hola! ¿Dónde estoy?"
# [toktok.tokenize(sent) for sent in sent_tokenize(sentences, language='spanish')]
# result = '\n'.join([' '.join(toktok.tokenize(sent)) for sent in sent_tokenize(sentences, language='spanish')])
# print (result)



# from stopwords_ca import get_stopwords 
# # degut a que sembla que la llibreria nltk està millor desenvolupada que stop_words, 
# # apliquem una conjunció de les dues (per aprofitar stopwords que tenen en comú ambdos idiomes)
# stop_wordsC = get_stopwords()
# print (stop_wordsC)

# from nltk.stem import SnowballStemmer
# print(" ".join(SnowballStemmer.languages))

# import subprocess
# args = ("/home/sergi/snowball/stemwords", "-l", "catalan", "-i", "TrainingDataSet/resultsPreprocess.csv", "-o", "TrainingDataSet/stemmed.csv")
# popen = subprocess.Popen(args, stdout=subprocess.PIPE)
# popen.wait()

# import subprocess
# args = ("/home/sergi/snowball/stemwords", "-l", "catalan", "-i", "JocsDeProves/testPreprocess.csv", "-o", "JocsDeProves/stemmedTest.csv")
# popen = subprocess.Popen(args, stdout=subprocess.PIPE)
# popen.wait()
# tlist = []
# with open('TrainingDataSet/stemmed.csv') as f:
#   reader = csv.reader(f)
#   for row in reader:
#     tlist.append((','.join(row), ['TI']))
          
# print (tlist[:2])

# import pandas as pd
# # data = pd.read_csv('TrainingDataSet/trainingBO.csv', sep = '/n', names=['Text', 'Class'], engine='python')
# data = pd.read_csv('/home/sergi/CityRoad_Disruptions/Proves/TrainingDataSet/trainingDataSet.csv', sep = '\t', lineterminator='\n')
# for index, row in data.iterrows():
#     print(row['Text'])