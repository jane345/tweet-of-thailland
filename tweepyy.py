from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from TwitterAPI import TwitterAPI
from firebase import firebase
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time
firebase = firebase.FirebaseApplication('https://tweet-of-thailand.firebaseio.com', None)
consumer_key = "LEIS7RiIlCxxKVvTMLwdTkl68"
consumer_secret = "Qx4HG9Arr2txdvEmhgxq2HckpuxXEAMIPYczLAW32dWZB6WHq9"
access_token_key = "1258970233-QJg3tFNji6SqRKSjP60NvCZysFBYjZ9xitr87dt"
access_token_secret = "6YwDy6P5oL7aFssVm1FmRvranSdOBwmq6wOujp2SUu2aW"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
# auth = OAuthHandler(consumer_key, consumer_secret)
# api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
# runtime = 10 #this means one minute
# r = api.request('statuses/filter', {'track': 'food'})

# for item in r:
#         print(item['text'] if 'text' in item else item)
#         #print('--------------------------------------')

class MyStreamListener(StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
        # record = {'Text': status.text, 'Created At': status.created_at}
        # print(record) #See Tweepy documentation to learn how to access other fields
        self.num_tweets += 1
        if self.num_tweets < 10:
            print('-------------------',self.num_tweets)
            if (not status.retweeted) and ('RT @' not in status.text):
                print(status.text)
            return True
        else:
            return False

# myStream = tweepy.Stream(auth=auth, listener=MyStreamListener(time_limit=60))
myStream = Stream(auth, MyStreamListener())
to_track = ['จตุจักร']
myStream.filter(track=to_track)






# '''Start streaming'''
# twitterstream = Stream(auth, TweetListener())
# twitterstream.filter(track=['twitter']) #apply any filter you want
# time.sleep(runtime) #halts the control for runtime seconds
# twitterstream.disconnect() #disconnect the stream and stop streaming


'''api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    r = api.request('statuses/filter', {'track': 'jane'})
    for item in r:
        #print(item['text'] if 'text' in item else item)
        #print('--------------------------------------')
        firebase.post('/tweet/',{'text': item['text']})
'''
