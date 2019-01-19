import sys
from Preprocess import *
from TopicModel import *

def listen (model):
    # connect to API twitter via Streaming and classify tweets.
    # if tweet == TI then call ARCGIS and locate. 
    return True

# error treatments
def main(args=sys.argv[1:]):
    df = args[0]
    dfprep = preprocess (df)
    # model = trainModel(dfprep)

    # listen (model)
    # showModel ()
    # testModel (args[2])
#  comprovacions dels resultats del model i comunicació amb API ARCGIS 

if __name__ == '__main__':
    main()