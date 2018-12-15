import nltk
import csv
import string
import re
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
tlist = []
with open('TrainingDataSet/stemmed.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    tlist.append((','.join(row), ['TI']))
          
print (tlist[:2])
