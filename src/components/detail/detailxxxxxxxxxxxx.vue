<template>
<div>
  <div class="ui raise segment" style="margin-right: auto; margin:0 auto; border-color:#27549E; padding:10px; max-width:80%; border-width: thick; background-color: rgba(0, 0, 0, 0.5);">
    <h1 class="ui top attached header" style="text-align:center; color:white; background-color:#27549E; border-color:#D2D0CF;">{{ $route.params.landmark }}</h1>
  </div>
    <div class="ui very relaxed stackable grid">
      <div class="twelve wide column">
      <div class="ui segment" style="margin-right: 0%; margin-left: 3%; max-width: 100%">
    <div class="center aligned ui grid">
        <div class="four wide column">
          <a class="ui huge label" @click="Select('news')">
          <img class="ui right spaced avatar image" :src="'static/news.png'">
          News
          </a>
        </div>
        <div class="four wide column">
          <a class="ui huge label" @click="Select('food')">
          <img class="ui right spaced avatar image" :src="'static/food.png'">
          Food
          </a>
        </div>
        <div class="four wide column">
          <a class="ui huge label" @click="Select('environment')">
          <img class="ui right spaced avatar image" :src="'static/envi.png'">
          Environment
          </a>
        </div>
        <div class="four wide column">
          <a class="ui huge label" @click="Select('traffic')">
          <img class="ui right spaced avatar image" :src="'static/traffic.png'">
          Traffic
          </a>
        </div>
    </div>
    <div class="ui three column grid">
      <div class="column">
        <h3 class="ui header" style="background-color:#70C27E;">Positive</h3>
        {{sentiment}}
      </div>
      <div class="column">
        <h3 class="ui header" style="background-color:#FAD836;">Neutral</h3>
        {{sentiment}}
      </div>
      <div class="column">
        <h3 class="ui header" style="background-color:#F16043;">Negative</h3>
        {{sentiment}}
      </div>
    </div>
    </div> <!--div ui segment -->
    </div> <!-- twelve column -->
    <div class="four wide column" style="padding: 0;">
    <div class="ui segment" style="width:100%; margin-left: 0;">
        <div class="image">
            <img :src="'static/central.jpeg'">
          </div>
        </div>
      </div>
  </div> <!-- two stack -->
  <button @click="send()">Send Request</button>
  <button @click="cancel()">Cancel Request</button>
  {{messagee}}
</div>
</template>

<script>
// import {fire} from './firebase'
// import axios from 'axios'
import Request from 'axios-request-handler'
const reviews = new Request('http://localhost:5000/tweet')
// const CancelToken = axios.CancelToken
// const source = CancelToken.source()
// var ref = fire.database().ref('tweet')
export default {
  data () {
    return {
      sentiment: '',
      detail: '',
      center: { lat: 13.746909, lng: 100.539329 },
      markers: [],
      places: [],
      currentPlace: null,
      infowindow: { lat: 13.746909, lng: 100.539329 },
      window_open: false,
      messagee: '',
      twit: [],
      check: 0
    }
  },
  methods: {
    send () {
      // this.messagee = 'Request is beign executed...'
      // axios.get('http://localhost:5000/tweet')
      //   .then((response) => {
      //     this.messagee = 'The response from server is:' + response
      //   })
      while (this.check === 0) {
        reviews.get()
          .then((res) => {
            this.messagee = 'The response from server is:' + res
            console.log(res.data.status)
          })
      }
    },
    cancel () {
      this.check = 1
    },
    /*
    gettweet () {
      const path = 'http://localhost:5000/tweet'
      axios.get(path)
        .then((res) => {
          // this.books = res.data.books
          console.log('tweet')
          ref.orderByKey().on('child_added', function (snapshot) {
            console.log(snapshot.key)
          })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    }, */
    Select (topic) {
      this.sentiment = topic
    }
  },
  created () {
  },
  mounted () {
    // this.addMarker()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style>
/*
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
*/
h3 {
  text-align: center;
}
img {
  width: 80%;
}
</style>
