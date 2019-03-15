import sys
from Preprocess import *
from TopicModel import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from GeoCoding import *
from Twitter import *

def init (model):
    return True

def main(args=sys.argv[1:]):
    df = args[0]
    gc = Geocoder()
    svm = SVMmodel()
    preprocess (df)
    twitter = Twitter()
    isIT = svm.predictText(tweet)
    gc.geoCode(tweet)

    
if __name__ == '__main__':
    main()