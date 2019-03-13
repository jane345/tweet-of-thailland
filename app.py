from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from TwitterAPI import TwitterAPI
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
from firebase import firebase
import pyrebase
import time

# ////////////////////////////
import tensorflow as tf
from sklearn import svm
from sklearn.svm import SVC
import numpy as np
import project
import embedded
import pickle
# ////////////////////////////////

firebase = firebase.FirebaseApplication('https://tweet-of-thailand.firebaseio.com', None)

consumer_key = "LEIS7RiIlCxxKVvTMLwdTkl68"
consumer_secret = "Qx4HG9Arr2txdvEmhgxq2HckpuxXEAMIPYczLAW32dWZB6WHq9"
access_token_key = "1258970233-QJg3tFNji6SqRKSjP60NvCZysFBYjZ9xitr87dt"
access_token_secret = "6YwDy6P5oL7aFssVm1FmRvranSdOBwmq6wOujp2SUu2aW"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
# app.config.from_object(__name__)
global graph,model_sentiment,model_subject
model_sentiment = pickle.load(open("E:\\Senior_Project\\1_code\\deep\\website(vue)\\my-project\\SVM_linear_new.pkl", 'rb'))
model_subject = pickle.load(open("E:\\Senior_Project\\1_code\\deep\\website(vue)\\my-project\\subject_rbf_multi.pkl", 'rb'))
graph = tf.get_default_graph()
arr = []
class MyStreamListener(StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_status(self, status):
        global arr
        self.num_tweets += 1
        print(arr)
        if self.num_tweets < 5:
            # if (not status.retweeted) and ('RT @' not in status.text):
                # firebase.post('/tweets/',{ 'tweet': status.text })
            if (status.text in arr):
                print('duplicate')
            else:
                print(status.text)
                arr.append(status.text)
            return True
        else:
            classify(arr)
            arr = []
            return False

def classify(status):
    print('feed to model')
    with graph.as_default():
        for i in range(0,len(status)):
            print(i,': ',status[i])
            token = project.tokenized_word(status[i])
            embedded_vec = embedded.embedded_word(token).reshape(1,-1)
            
            predict_sentiment = model_sentiment.predict_proba(embedded_vec)
            predict_subject = model_subject.predict(embedded_vec)
            
            sentiment = np.array2string(np.argmax(predict_sentiment))
            subject = np.array2string(np.argmax(predict_subject))
            
            firebase.post('/tweets/',{ 'tweet': status[i], 'sentiment': sentiment, 'subject': subject })
            print('write '+ status[i] + ' to firebase ')

@app.route('/tweet', methods=['GET'])
def getTweet():
    print('request from web')
    arr
    myStream = Stream(auth, MyStreamListener())
    myStream.filter(track=[str(request.args.get('landmark'))])
    # for i in range (0,1):
    #     firebase.post('/tweets/',{ 'tweet': request.args.get('landmark') })
    #     # firebase.post('/tweet/s',{ 'tweets': item['text']})
    #     time.sleep(2)
    return 'write in firebase'

if __name__ == '__main__':
    app.run(debug=True)