import csv
import string
import nltk
import re
# import stop_words
from nltk import sent_tokenize
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import TweetTokenizer


with open('resultsTransitComplete1.csv') as f:
  reader = csv.reader(f)
  i = 10
  for row in reader:
    # print (row[1])
    # sentences = sent_tokenize(row[1])
    # print sentences
    # print "ESPAAAAAAI"

    # Tokenize tweets. Word splitting.
    # from nltk.tokenize.toktok import ToktokTokenizer
    toktok = ToktokTokenizer()
    tokens = toktok.tokenize(row)
    table = str.maketrans('', '', string.punctuation)
    words = [w.translate(table) for w in tokens]

    # Remove hyperlinks
    list_no_hyperlinks=[re.sub(r'https?:\/\/.*\/\w*','',i) for i in words]
    # print('No hyperlinks:')
    # print(list_no_hyperlinks)
    # Remove hashtags
    list_no_hashtags=[re.sub(r'#', '', i) for i in list_no_hyperlinks]
    # print('No hashtags:')
    # print(list_no_hashtags)


    # Filter only if word is alphabetic characters only. (fer que AP-7 també estigui acceptat -> guions i numeros)
    words = [word for word in list_no_hashtags if word.isalnum()]
    # print ("AIXÒ SÓN WORDS FINALS:")
    # words (words)
    #convert to lowercase
    words = [word.lower() for word in words]


    from stopwords_ca import get_stopwords 
    # hem agafat els stop_words de http://latel.upf.edu/morgana/altres/pub/ca_stop.htm (ens hem fet la nostra propia funció)
    stop_words = get_stopwords()
    words = [w for w in words if not w in stop_words]
    print (words)
    # Stemming
    # from nltk.stem.porter import PorterStemmer
    # porter = PorterStemmer()
    # stemmed = [porter.stem(word) for word in words]
    # print(stemmed)
    
    
    if (i<0): break
    else: i = i-1
