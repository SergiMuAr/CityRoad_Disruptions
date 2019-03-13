import sys
from Preprocess import *
from TopicModel import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from GeoCoding import *

def listen (model):
    # connect to API twitter via Streaming and classify tweets.
    # if tweet == TI then call ARCGIS and locate. 
    return True

# error treatments
def main(args=sys.argv[1:]):
    df = args[0]
    preprocess (df)
    svm = SVMmodel()
    tweet = "➡️Retencions a la Ronda litoral de Zona Franca a Can Tunis -&gt;"
    isTI = svm.predictText(tweet)
    if (isTI):
        gc = Geocoder()
        gc.geoCode(tweet)
    

if __name__ == '__main__':
    main()