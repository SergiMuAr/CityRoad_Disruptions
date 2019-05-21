import csv
import string
import nltk
import re
import pandas as pd
from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class NLP:
    def __init__(self):
        self.tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))

    def prepareToClf (self,text):
        txt = str(text)
        # Tokenize tweets. Word splitting.
        exclusionList = [r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b','-&gt']
        exclusions = '|'.join(exclusionList)
        txt = re.sub(exclusions, '', ''.join(txt).rstrip(), flags=re.MULTILINE)
        toktok = ToktokTokenizer()
        tokens = toktok.tokenize(txt)
        words = tokens
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
        table = str.maketrans('', '', ''.join([string.punctuation,"’"]))
        words = [w.translate(table) for w in words]

        import unidecode
        unaccented_string = unidecode.unidecode(','.join(words))
        return self.tf_vectorizer.transform([unaccented_string]).toarray()


    def prepareToVisualize(self,tweet):
        exclusionList = [r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b','-&gt', "'"]
        exclusions = '|'.join(exclusionList)
        txt = re.sub(exclusions, '', ''.join(tweet).rstrip(), flags=re.MULTILINE)
        return txt
    
    def tfidf(self):
        data = pd.read_csv('DataSet/preprocessed.csv', sep = '\t', lineterminator='\n')
        text = data['Text']
        target = data['Class']
        train_matrix = self.tf_vectorizer.fit_transform(text.values.astype('U')).toarray()
        return train_matrix, target
# nlp = NLP()
# print (nlp.prepareToClf("""🚗Cues als principals accessos a BCN. Pel nord: 
# ➡️C-58 Terrassa Est-Badia/Montcada -> BCN
# Montcada-Ripollet -> Terrassa
# ➡️C-16 peatge-boca nord Túnel Vallvidrera 
# ➡️C-31 nord a Badalona  
# #equipviari"""))