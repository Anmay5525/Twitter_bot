from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

consumerKey = "49qN5k1Trnz060Bp1MdgzYD4s"
consumerSecret = "MtumQPNeToT7c3aGEtIsdfdw5J4ADR0C9c21irPYC3FoQNFms6"
accessToken = "1009111317024792576-Nz2evvUeDWi1ZQh9wm1HoCeXVsWCDG"
accessTokenSecret = "3BneR1cAlUgAOX54nU4J1g5E5ZU317QulsU3KWT0HHTzY"

auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken , accessTokenSecret)
api = tweepy.API(auth)

"""me = api.me()
print(me.name)
"""
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
