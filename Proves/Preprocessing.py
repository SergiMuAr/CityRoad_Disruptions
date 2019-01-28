import csv
import string
import nltk
import re

from nltk import sent_tokenize
from nltk.tokenize.toktok import ToktokTokenizer

csvFile = open('TrainingDataSet/stemmedNTI.csv', 'w')
csvWriter = csv.writer(csvFile)
# NETEJAR -&gt DE LES DADES.

with open('TrainingDataSet/trainingDataSet.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    # print (row[1])
    # sentences = sent_tokenize(row[1])
    # print sentences
    # print "ESPAAAAAAI"
    # Tokenize tweets. Word splitting.
    from nltk.tokenize.toktok import ToktokTokenizer
    toktok = ToktokTokenizer()
    row = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', ''.join(row).rstrip(), flags=re.MULTILINE)

    tokens = toktok.tokenize(row)
    words = tokens
    table = str.maketrans('', '', ''.join([string.punctuation,"’"]))
    words = [w.translate(table) for w in tokens]

    # Filter only if word is alphabetic characters only. (fer que AP-7 també estigui acceptat -> guions i numeros)
    # words = [word for word in words if word.isalnum()]
    # print ("AIXÒ SÓN WORDS FINALS:")
    # words (words)
    #convert to lowercase
    words = [word.lower() for word in words]


    from stopwords_ca import get_stopwords 
    emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        "]+", flags=re.UNICODE)
    # hem agafat els stop_words de http://latel.upf.edu/morgana/altres/pub/ca_stop.htm (ens hem fet la nostra propia funció)
    stop_words = get_stopwords()
    words = [emoji_pattern.sub(r'', w) for w in words if not w in stop_words] # NO EMOJI

    # Stemming
    # from nltk.stem.porter import PorterStemmer
    # porter = PorterStemmer()
    # stemmed = [porter.stem(word) for word in words]
    # print(stemmed)

    # import subprocess
    # args = ("./stemwords", "-l", "cat", "-i", "input_file.txt", "-o", "output_file.txt")
    # popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    # popen.wait()

    # For "unixy" systems like linux and OSX, the pexpect module is written to handle the complexities of an interactive child process. 
    # For Windows, there is no good tool that I know of to do it.
    # import subprocess
    # p = subprocess.Popen(['/home/sergi/snowball/stemwords', '-l', 'catalan'],
    #                   stdin=subprocess.PIPE,
    #                   stdout=subprocess.PIPE,
    #                   universal_newlines=True)
    # for w in words:
    #   stdout_data, stderr_data = p.communicate(''.join(w))
    #   print(stdout_data)
    #   p.wait()


    # LEMMATIZER
    #encoding: utf8
    # with open('lemmatization-es.txt', 'rb') as f:
    #   data = f.read().decode('utf8').replace(u'\r', u'').split(u'\n')
    #   data = [a.split(u'\t') for a in data]
      
    # lemmaDict = { a[1]:a[0] for a in data if len(a)>1 }
    # lemmaDict.update( { a:a for a in set(lemmaDict.values()) } )
      
    # def lemmatize(word):
    #   return lemmaDict.get(word, word + u'*')
      
    # def test():
    #   for a in [ u'salió', u'usuarios', u'abofeteéis', u'diferenciando', u'diferenciándola' ]:
    #       print(lemmatize(a))
    
    # Treure ascii
    # words = [w.encode('ascii', 'ignore').decode('ascii') for w in words]
    csvWriter.writerow(words)
   
csvFile.close()
# # Stemmer
# import subprocess
# args = ("/home/sergi/snowball/stemwords", "-l", "catalan", "-i", "TrainingDataSet/preprocessTraining.csv", "-o", "TrainingDataSet/stemmed.csv")
# popen = subprocess.Popen(args, stdout=subprocess.PIPE)
# popen.wait()


# csvFile = open('TrainingDataSet/stemmedllda.csv', 'w')
# csvWriter = csv.writer(csvFile)
# with open('TrainingDataSet/stemmed.csv') as f:
#   reader = csv.reader(f)
#   for row in reader:
#     csvWriter.writerow((','.join(row), ['TI']))
      
        