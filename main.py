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
    model = trainModel()
    tf_vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2))
    tweet = "heeeelooou estic parlant de qualssevol parida que no és el tema"
    test_tweet = tf_vectorizer.transform([tweet]).toarray()
    print(model.predict(test))
    # listen (model)
    # showModel ()
    # testModel (args[2])
#  comprovacions dels resultats del model i comunicació amb API ARCGIS 

if __name__ == '__main__':
    main()