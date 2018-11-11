import csv
import string
import nltk
import stop_words
from nltk import sent_tokenize
from nltk.tokenize.toktok import ToktokTokenizer


with open('resultsTransitComplete1.csv') as f:
  reader = csv.reader(f)
  i = 10
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
    
    if (i<0): break
    else: i = i-1
