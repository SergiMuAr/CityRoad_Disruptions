import csv
import string
import nltk
import re
import pandas as pd
from nltk.tokenize.toktok import ToktokTokenizer


def preprocessText (text):
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
    return unaccented_string
