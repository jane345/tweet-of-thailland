import * as firebase from 'firebase/app'
import 'firebase/database'
import '@firebase/firestore'
var config = {
  apiKey: 'AIzaSyAcTFcNCUsmqw8JWClDKJuHWHzF8LOcpgY',
  authDomain: 'tweet-of-thailand.firebaseapp.com',
  databaseURL: 'https://tweet-of-thailand.firebaseio.com',
  projectId: 'tweet-of-thailand',
  storageBucket: 'tweet-of-thailand.appspot.com',
  messagingSenderId: '63045280219'
}
var fire = firebase.initializeApp(config)
var db = firebase.firestore()
export {fire, db}
