import sys
from Preprocess import *
from TopicModel import *
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def listen (model):
    # connect to API twitter via Streaming and classify tweets.
    # if tweet == TI then call ARCGIS and locate. 
    return True

# error treatments
def main(args=sys.argv[1:]):
    df = args[0]
    preprocess (df)
    model = SVMmodel.trainModel()
    tweet = "heeeelooou estic parlant de qualssevol parida que no és el tema"
    SVMmodel.predictText(tweet)
    # listen (model)
    # showModel ()
    # testModel (args[2])
#  comprovacions dels resultats del model i comunicació amb API ARCGIS 

if __name__ == '__main__':
    main()