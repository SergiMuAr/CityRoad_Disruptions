import csv
import string
import nltk
import re

from nltk.tokenize.toktok import ToktokTokenizer


def preprocess (dataSet):
    csvFile = open('DataSet/Preprocessed/preprocessTraining.csv', 'w')
    csvWriter = csv.writer(csvFile)
    with open(''.join(['DataSet/Training/', dataSet])) as f:
        reader = csv.reader(f)
        for row in reader:

            # Tokenize tweets. Word splitting.
            toktok = ToktokTokenizer()
            row = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', ''.join(row).rstrip(), flags=re.MULTILINE)
            tokens = toktok.tokenize(row)
            words = tokens
            table = str.maketrans('', '', string.punctuation)
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


            csvWriter.writerow(words)
    
    csvFile.close()
    return csvFile

# Stemmer
def _stemmer():
    import subprocess
    args = ("/home/sergi/snowball/stemwords", "-l", "catalan", "-i", "TrainingDataSet/preprocessTraining.csv", "-o", "TrainingDataSet/stemmedBFN.csv")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
