from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

consumerKey = "Your consumer key"
consumerSecret = "Your consumer secret key"
accessToken = "access token of twitter app"
accessTokenSecret = "access token secret of twitter app"

auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken , accessTokenSecret)
api = tweepy.API(auth)

"""
for tweet in tweepy.Cursor(api.search, "fortnite", result_type = "recent", lang = "en").items(10) :
    print(tweet.user.screen_name)
    print(tweet.text)
 """
def follow_all():
    for followers in tweepy.Cursor(api.followers).items():
        followers.follow()
        print("Followed " + followers.user.screen_name)


def fav_tweet(query, count):
    for tweet in tweepy.Cursor(api.search, query, result_type = "recent", lang = "en").items(count) :
        try:
            tweet.favorite()
            print('Favorited the tweet' + tweet.text)
        
        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break
        
def retweet(query, count):
    for tweet in tweepy.Cursor(api.search, query, result_type = "recent", lang = "en").items(count) :
        try:
            tweet.retweet()
            print('Retweeted the tweet ' + tweet.text)
        
        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break

def reply_all(text, query, count):
    for tweet in tweepy.Cursor(api.search, query, result_type = "recent", lang = "en").items(count):
        try:
            id = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + query + " " + text, in_reply_to_status_id = id )
            print("replied to " + username)
            
        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break
        
        
while(1):
    
    try:
        follow_all()
        retweet("csgo", 1)

    except tweepy.TweepError as e :
        print(e.reason)

    try:
        fav_tweet("fortnite", 1)

    except tweepy.TweepError as e :
        print(e.reason)

    try:
        reply_all("Dominated by Astralis","#csgo", 1)

    except tweepy.TweepError as e :
        print(e.reason)
