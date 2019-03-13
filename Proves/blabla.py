from streaming import *

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# myStream.filter(locations = [3.28, 42.41, 0.49, 40.54]) #track = ['python'] #async = True?
myStream.filter(locations = [0.49, 40.54, 3.28, 42.41]) #track = ['python'] #async = True?

# myStream.filter(locations=[-6.38,49.87,1.77,55.81]) #track = ['python'] #async = True?
