import sys
from Preprocess import *
from TopicModel import *

# error treatments
def main(args=sys.argv[1:]):
    dprep = preprocess (args[0])
    trainModel()
    # showModel ()
    # testModel (args[2])
#  comprovacions dels resultats del model i comunicació amb API ARCGIS 

if __name__ == '__main__':
    main()