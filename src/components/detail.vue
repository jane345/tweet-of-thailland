<template>
<div>
  <div class="ui inverted segment">
      <button class="tiny ui blue button"  style="margin-bottom: 5px; font-family: 'Caveat Brush', cursive; font-size: 1.25vw;" @click="Back()"><i class="angle left icon"></i>Back</button>
      <button class="tiny ui blue button"  style="margin-bottom: 5px; font-family: 'Caveat Brush', cursive; font-size: 1.25vw;"  @click="gotoHome()"><i class="home icon"></i>Home</button>
  </div>
  <div class="ui raise segment" style="margin: auto; border-color:#27549E; padding:10px;  max-width:95%; border-width: thick; background-color: rgba(0, 0, 0, 0.5);">
    <div class="ui very relaxed stackable grid">
      <div class="four wide column" style="padding-right: 0;">
    <h1 class="ui top attached header">
      {{ $route.params.landmark }}
    </h1>
      </div>
      <div class="twelve wide column" style="padding-left: 1%;">
    <div class="ui segment" style="margin: auto; font-family: 'Athiti', sans-serif; font-size: 1.5vw;">
      <p>{{detail}}</p>
    </div>
      </div>
  </div>
  </div>
    <div class="ui very relaxed stackable grid">
      <div class="thirteen wide column">
      <div class="ui segment" style="margin: 1%; max-width: 100%">
    <div class="center aligned ui grid" style="margin-bottom: 0;" id="kk">
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="calltweet('news')">
          <img class="ui right spaced avatar image" :src="'/static/news.png'">
          News
          </a>
        </div>
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="calltweet('food')">
          <img class="ui right spaced avatar image" :src="'/static/food.png'">
          Food
          </a>
        </div>
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="calltweet('environment')">
          <img class="ui right spaced avatar image" :src="'/static/envi.png'">
          Environment
          </a>
        </div>
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="calltweet('traffic')">
          <img class="ui right spaced avatar image" :src="'/static/traffic.png'">
          Traffic
          </a>
        </div>
    </div>
    <div class="ui three column grid"  style="margin-top: 0;">
      <div class="column" style="margin-top: 0;">
        <h3 class="ui header" style="background-color:#70C27E;">Positive</h3>
        <ul id="list_positive" style="padding-left: 0;">
        </ul>
      </div>
      <div class="column" style="margin-top: 0;">
        <h3 class="ui header" style="background-color:#FAD836;">Neutral</h3>
        <ul id="list_neutral" style="padding-left: 0;">
        </ul>
      </div>
      <div class="column" style="margin-top: 0;">
        <h3 class="ui header" style="background-color:#F16043;">Negative</h3>
        <ul id="list_negative" style="padding-left: 0;">
        </ul>
      </div>
    </div>
    </div> <!--div ui segment -->
    </div> <!-- thirteen column -->
    <div class="three wide column" style="padding-left: 0">
    <div class="center aligned ui segment" style="width:100%; height: 500px; margin-left: 0;">
      <!-- <div class="zoom"> -->
        <!-- <a href="https://twitter.com/drballban/status/1095374690862788608"> -->
          <!-- <img :src="'/static/central.jpeg'"></a> -->
          <!-- <img v-for="(ind,index) in loop" :key="index" :src="'/static/'+ $route.params.landmark + '/' + ind + '.jpg'"> -->
          <!-- <span><img :src="'/static/central.jpeg'" alt="image"></span>
          </a> -->
          <!-- imageeeeeeeeeeeeeeeeeeeeeeeee -->
          <!-- <div :key="key" v-for="(ind, key) in loop" >
            <img :src="'/static/'+ $route.params.landmark + '/' + ind + '.jpg'" class="zoom" >
          </div> -->
          <!-- imageeeeeeeeeeeeeeeeeeeeeeeeee -->
        </div>
      </div>
  </div> <!-- two stack -->
  <!-- mapppppppppppppppppppppppppppppppppppppppp -->
  <div id="map" style="width: 60%; height: 400px; margin: auto;"></div>
</div>
</template>

<script src="http://maps.google.com/maps/api/js?sensor=false"></script>
<script>
import {fire} from './firebase'
import Request from 'axios-request-handler'
import axios from 'axios'
const reviews = new Request('http://localhost:5000/tweet')
var Url = 'http://localhost:5000/tweet'
export default {
  data () {
    return {
      sentiment: [],
      subject: '',
      sub: '',
      detail: '',
      center: {lat: 0, lng: 0}, // { lat: 13.746909, lng: 100.539329 },
      markers: [],
      currentPlace: {lat: 0, lng: 0},
      loop: [1, 2],
      SendInterval: '',
      NewsInterval: '',
      FoodInterval: '',
      EnvironmentInterval: '',
      TrafficInterval: ''
    }
  },
  methods: {
    Back () {
      var tweetRef = fire.database().ref('tweets/')
      tweetRef.remove()
      clearInterval(this.SendInterval)
      clearInterval(this.NewsInterval)
      clearInterval(this.FoodInterval)
      clearInterval(this.EnvironmentInterval)
      clearInterval(this.TrafficInterval)
      this.$router.go(-1)
      this.SendtoPython(0)
    },
    gotoHome () {
      this.$router.replace('/')
      this.SendtoPython(0)
    },
    calltweet (subject) {
      // this.subject = sub
      clearInterval(this.NewsInterval)
      clearInterval(this.FoodInterval)
      clearInterval(this.EnvironmentInterval)
      clearInterval(this.TrafficInterval)
      document.getElementById('list_negative').innerHTML = ''
      document.getElementById('list_neutral').innerHTML = ''
      document.getElementById('list_positive').innerHTML = ''
      if (subject == 'news') {
        this.DisplayTweet(0)
        this.NewsInterval = setInterval(this.DisplayTweet.bind(null,0), 10000)
      } else if (subject == 'food') {
        this.DisplayTweet(1)
        this.FoodInterval  = setInterval(this.DisplayTweet.bind(null,1), 10000)
      } else if (subject == 'environment') {
        this.DisplayTweet(2)
        this.EnvironmentInterval = setInterval(this.DisplayTweet.bind(null,2), 10000)
      } else if (subject == 'traffic') {
        this.DisplayTweet(3)
        this.TrafficInterval = setInterval(this.DisplayTweet.bind(null,3), 10000)
      }
    },
    DisplayTweet: function (sub) {
      // this.sub = sub
      var tweetRef = fire.database().ref('tweets/')
      const arr_pos = [], arr_neu = [], arr_neg = []
      var i=0
      tweetRef.once('value', (snapshot) => {
        snapshot.forEach((childSnapshot) => {
          if (childSnapshot.val().sentiment == 0 && childSnapshot.val().subject == sub) {
            arr_pos.push(childSnapshot.val().tweet)
            this.Positive(arr_pos)
          }
          else if (childSnapshot.val().sentiment == 1  && childSnapshot.val().subject == sub) {
            arr_neu.push(childSnapshot.val().tweet)
            this.Neutral(arr_neu)
          }
          else if (childSnapshot.val().sentiment == 2  && childSnapshot.val().subject == sub) {
            arr_neg.push(childSnapshot.val().tweet)
            this.Negative(arr_neg)
          }
        })
      })
    },
    Positive (arr) {
      document.getElementById('list_positive').innerHTML = ''
      for (var i=0; i<arr.length; i++) {
        var node = document.createElement('div')
        node.className = 'ui inverted segment'
        var textnode = document.createTextNode(arr[i])
        node.appendChild(textnode)
        document.getElementById('list_positive').appendChild(node)
      }
    },
    Neutral (arr) {
      document.getElementById('list_neutral').innerHTML = ''
      for (var i=0; i<arr.length; i++) {
        var node = document.createElement('div')
        node.className = 'ui inverted segment'
        var textnode = document.createTextNode(arr[i])
        node.appendChild(textnode)
        document.getElementById('list_neutral').appendChild(node)
      }
    },
    Negative (arr) {
      document.getElementById('list_negative').innerHTML = ''
      for (var i=0; i<arr.length; i++) {
        var node = document.createElement('div')
        node.className = 'ui inverted segment'
        var textnode = document.createTextNode(arr[i])
        node.appendChild(textnode)
        document.getElementById('list_negative').appendChild(node)
      }
    },
    SendtoPython (status) {
      axios({
        method: 'get',
        url: Url,
        headers: {
          'Accept': 'application/json'
        },
        useCredentails: true,
        params: {
          landmark: this.$route.params.landmark,
          status: status
          }
      })
        .then(function (response) {
          console.log(response)
        })
    }
  },
  mounted () {
    this.SendtoPython(1)
    // this.SendInterval = setInterval(this.SendtoPython,60000)
    this.$gmapApiPromiseLazy().then(() => {
      var directionsService = new google.maps.DirectionsService()
      var directionsDisplay = new google.maps.DirectionsRenderer({ suppressMarkers: true })
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: this.center
      })
      var marker = new google.maps.Marker({
        position: this.center,
        map: map,
        title: this.$route.params.landmark
      })
      navigator.geolocation.getCurrentPosition(position => {
        this.currentPlace = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        }
        var request = {
          origin: this.currentPlace,
          destination: this.center,
          travelMode: google.maps.DirectionsTravelMode.DRIVING
        }
        directionsDisplay.setMap(map)
        directionsService.route(request, function(response, status) {
          if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response)
          }
        })
      })
    })
  },
  created () {
    var ref = fire.database().ref('region/' + this.$route.params.regionName + '/' + this.$route.params.landmark)
    ref.on('value', (snapshot) => {
      this.center.lat = parseFloat(snapshot.val().lat)
      this.center.lng = parseFloat(snapshot.val().lng)
      this.detail = snapshot.val().detail
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style>
.ui.huge.label {
  font-family: 'Barlow Condensed', sans-serif;
  font-weight: bold;
  font-size: 1.2vw;
}
.ui.top.attached.header{
  font-family: 'Caveat Brush', cursive ,'Athiti', sans-serif;
  text-align:center;
  color:white;
  background-color:#27549E;
}
.ui.header {
  font-family: 'Barlow Condensed', sans-serif;
  font-weight: bold;
  font-size: 1.5vw;
}
h3 {
  text-align: center;
}
img {
  width: 60%;
}
.zoom {
  transition: transform .2s; /* Animation */
}

.zoom:hover {
  position: absolute;
  transform: scale(2);
  transform-origin: center right;
  z-index: 99;
  /* (2000% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}
ul > .ui.inverted.segment {
   margin-bottom: 0;
   margin-top: 1px;
   background-color: #38A1F3 !important;
   /* #80B8c3 */
}
</style>
