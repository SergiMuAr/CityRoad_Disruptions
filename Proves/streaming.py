import tweepy
import csv
auth = tweepy.OAuthHandler("Hdah781zeulKrfrMzK3iI6GTs", "tFLvGas5hrXwq4yiXheQj5On99VUoAl5Fpcl6vRQqatjxISFDZ")
auth.set_access_token("988457597241118720-NIGfC9gqlNakSIcmDZfVAvb5LZHDgqa", "SyoofoDP3GJsDhRFHdjjsIMAFLp2XwBYXakVyUhb3YvAE")

api = tweepy.API(auth)

print (api)

# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit').items():
#     print (status._json['text'])

# Open/create a file to append data to
csvFile = open('buenafuente.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

# # Els RT's no els retorna sencers moltes vegades
# for status in tweepy.Cursor(api.user_timeline, screen_name='@transit', tweet_mode = 'extended').items(500):
#     # Write a row to the CSV file. I use encode UTF-8
#     # csvWriter.writerow([tweet.created_at, tweet.text])
#     print (status.full_text)
# csvFile.close()
for tweet_info in tweepy.Cursor(api.user_timeline, screen_name='@Buenafuente', tweet_mode='extended').items(49):
    if 'retweeted_status' in dir(tweet_info):
        tweet=tweet_info.retweeted_status.full_text
    else:
        tweet=tweet_info.full_text
    print (tweet)
    csvWriter.writerow([tweet])
csvFile.close()
