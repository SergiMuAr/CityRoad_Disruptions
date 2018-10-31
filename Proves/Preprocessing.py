import csv
import string
import nltk
# import stop_words
from nltk import sent_tokenize
from nltk.tokenize.toktok import ToktokTokenizer

# Open/create a file to append data to
csvFile = open('resultsPreprocess.csv', 'a')
csvWriter = csv.writer(csvFile)

with open('resultsTransitComplete1.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    # print (row[1])
    # sentences = sent_tokenize(row[1])
    # print sentences
    # print "ESPAAAAAAI"

    # Tokenize tweets. Word splitting.
    from nltk.tokenize.toktok import ToktokTokenizer
    toktok = ToktokTokenizer()
    tokens = toktok.tokenize(row)
    table = str.maketrans('', '', string.punctuation)
    words = [w.translate(table) for w in tokens]

    # Filter only if word is alphabetic characters only. (fer que AP-7 també estigui acceptat -> guions i numeros)
    words = [word for word in words if word.isalnum()]
    # print ("AIXÒ SÓN WORDS FINALS:")
    # words (words)
    #convert to lowercase
    words = [word.lower() for word in words]


    from stopwords_ca import get_stopwords 
    # hem agafat els stop_words de http://latel.upf.edu/morgana/altres/pub/ca_stop.htm (ens hem fet la nostra propia funció)
    stop_words = get_stopwords()
    words = [w for w in words if not w in stop_words]

    # Stemming
    from nltk.stem.porter import PorterStemmer
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in words]
    csvWriter.writerow(stemmed)

csvFile.close()   
