import tweepy
import csv
auth = tweepy.OAuthHandler("Hdah781zeulKrfrMzK3iI6GTs", "tFLvGas5hrXwq4yiXheQj5On99VUoAl5Fpcl6vRQqatjxISFDZ")
auth.set_access_token("988457597241118720-NIGfC9gqlNakSIcmDZfVAvb5LZHDgqa", "SyoofoDP3GJsDhRFHdjjsIMAFLp2XwBYXakVyUhb3YvAE")

api = tweepy.API(auth)


# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
#     print (status._json['text'])

# Open/create a file to append data to
csvFile = open('TwitterResults/searchTw2.csv', 'w')

#Use csv writer
csvWriter = csv.writer(csvFile)

# # Els RT's no els retorna sencers moltes vegades
# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit', tweet_mode = 'extended').items(500):
#     # Write a row to the CSV file. I use encode UTF-8
#     # csvWriter.writerow([tweet.created_at, tweet.text])
#     print (status.full_text)
# csvFile.close()
query = "incident OR incidència OR incidencia OR accident OR cues OR retencions OR aturats OR tall OR tallat OR tallada OR obres -filter:retweets since:2018-11-15 until:2018-12-3",
for tweet in tweepy.Cursor(api.search, q=query, geocode = "41.5,2.0,100km", exclude_replies = True, tweet_mode = "extended").items(500):
    # print (tweet.full_text)
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text) and tweet.metadata['iso_language_code']:
        csvWriter.writerow((tweet.id_str, tweet.full_text)) 

csvFile.close()
