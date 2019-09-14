import tweepy
import time
import sys
import os
from key import key

SCREEN_NAME = key['screen_name']
CONSUMER_KEY = key['consumer_key']
CONSUMER_SECRET = key['consumer_secret']
ACCESS_TOKEN = key['access_token']
ACCESS_TOKEN_SECRET = key['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#l_list = api.lists_all()
#print(l_list)
os.system('clear')

def like_home_timeline():
    k = 1
    h_timeline = api.home_timeline(count = 50)
    for tweet in h_timeline:
        if not tweet.favorited:
            print("[",k,"]",tweet.author._json['screen_name'], ":", tweet.text, "\n")
            k+=1
            api.create_favorite(tweet.id)
            time.sleep(15)
    print("[{}] likes in home_timeline".format(k))
    print("[60sec] Time out")
    time.sleep(60)

def count_like_list_timeline():
    k=0
    l_timeline = api.list_timeline('Spherastree', 'list', count=500)
    for status in l_timeline:
        if not status.favorited:
            k+=1
    return k

def count_like_hometimeline():
    k=0
    h_timeline = api.home_timeline(count=50)
    for tweet in h_timeline:
        if not tweet.favorited:
            k+=1
    return k

def like_list_timeline():
    l_timeline = api.list_timeline('Spherastree', 'list', count = 500)
    for status in l_timeline:
        if not status.favorited:
            print(status.author._json['screen_name'], ":", status.text, "\n")
            api.create_favorite(status.id)
            time.sleep(25)


if __name__ == "__main__":
        while (1):
            os.system('clear')
            try:
                if count_like_list_timeline() == 0:
                    print("You have 0 tweets to like in list_timeline\n")
                    #time.sleep(60)
                else:
                    #print("Do u want like {0} tweets?\n".format(count_like_list_timeline()))
                    #if input("Y/N?: ") == 'y' or 'Y':
                        like_list_timeline()
                if count_like_hometimeline() == 0:
                    print("You have 0 tweets to like in home_timeline\n")
                else:
                    like_home_timeline()
            except:
                print("Possibly Rate limited? Sleeping 60 seconds")
                time.sleep(60)



"""
for tweet in h_timeline:
    if not tweet.favorited:
        print(tweet.id, ":", tweet.text, "\n")
        api.create_favorite(tweet.id)
"""
