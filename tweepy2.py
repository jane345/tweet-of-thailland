from TwitterAPI import TwitterAPI
from firebase import firebase

firebase = firebase.FirebaseApplication('https://tweet-of-thailand.firebaseio.com', None)

consumer_key = "LEIS7RiIlCxxKVvTMLwdTkl68"
consumer_secret = "Qx4HG9Arr2txdvEmhgxq2HckpuxXEAMIPYczLAW32dWZB6WHq9"
access_token_key = "1258970233-QJg3tFNji6SqRKSjP60NvCZysFBYjZ9xitr87dt"
access_token_secret = "6YwDy6P5oL7aFssVm1FmRvranSdOBwmq6wOujp2SUu2aW"
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('statuses/filter', {'track': 'จตุจักร'})

for item in r:
    print(item['text'] if 'text' in item else item)
    print('--------------------------------------')
    # firebase.post('/tweet/',{'text': item['text']})

   