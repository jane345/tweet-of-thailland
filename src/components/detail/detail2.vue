<template>
<div>
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
      <div class="twelve wide column">
      <div class="ui segment" style="margin: 1%; max-width: 100%">
    <div class="center aligned ui grid" style="margin-bottom: 0;">
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="Select('news')">
          <img class="ui right spaced avatar image" :src="'/static/news.png'">
          News
          </a>
        </div>
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="Select('food')">
          <img class="ui right spaced avatar image" :src="'/static/food.png'">
          Food
          </a>
        </div>
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="Select('environment')">
          <img class="ui right spaced avatar image" :src="'/static/envi.png'">
          Environment
          </a>
        </div>
        <div class="four wide column" style="margin-bottom: 0;">
          <a class="ui huge label" @click="Select('traffic')">
          <img class="ui right spaced avatar image" :src="'/static/traffic.png'">
          Traffic
          </a>
        </div>
    </div>
    <div class="ui three column grid"  style="margin-top: 0;">
      <div class="column" style="margin-top: 0;">
        <h3 class="ui header" style="background-color:#70C27E;">Positive</h3>
        {{sentiment}}
      </div>
      <div class="column" style="margin-top: 0;">
        <h3 class="ui header" style="background-color:#FAD836;">Neutral</h3>
        {{sentiment}}
      </div>
      <div class="column" style="margin-top: 0;">
        <h3 class="ui header" style="background-color:#F16043;">Negative</h3>
        {{sentiment}}
      </div>
    </div>
    </div> <!--div ui segment -->
    </div> <!-- twelve column -->
    <div class="four wide column" style="padding-left: 0">
    <div class="ui segment" style="width:100%; margin-left: 0;">
      <div class="zoom">
        <a href="https://twitter.com/drballban/status/1095374690862788608">
          <img :src="'/static/central.jpeg'"></a>
          <!-- <span><img :src="'/static/central.jpeg'" alt="image"></span>
          </a> -->
      </div>
        </div>
      </div>
  </div> <!-- two stack -->
  <!-- mapppppppppppppppppppppppppppppppppppppppp -->
  <div id="map">
    <!-- <gmap-autocomplete @place_changed="setPlace"></gmap-autocomplete> -->
    <button @click="displayRoute"> Add  </button>
    <gmap-map ref="map" :center="center" :zoom="12"
    style="width:60%;  height: 300px; margin: auto;">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="center=m.position"
        :title="m.title"
      ></gmap-marker>
      <!-- @click="openWindow" -->
      <!-- <gmap-info-window
            @closeclick="window_open=false"
            :opened="window_open"
            :position="infowindow"
            :options="{
              pixelOffset: {
                width: 0,
                height: -35
              }
            }"
        >
        </gmap-info-window> -->
    </gmap-map>
  </div>
</div>
</template>

<script src="http://maps.google.com/maps/api/js?sensor=false"></script>
<script>
import {fire} from './firebase'
import {loaded} from 'vue2-google-maps'
export default {
  data () {
    return {
      sentiment: '',
      detail: '',
      center: {lat: 0, lng: 0}, // { lat: 13.746909, lng: 100.539329 },
      markers: [],
      places: [],
      currentPlace: null,
      infowindow: {}, // { lat: 13.746909, lng: 100.539329 },
      window_open: false
    }
  },
  methods: {
    openWindow () {
      this.window_open = true
    },
    Select (topic) {
      this.sentiment = topic
    },
    setPlace (place) {
      this.currentPlace = place
    },
    addMarker () {
      this.markers.push({
        position: this.center,
        title: this.$route.params.landmark })
      // ////////////
      // if (this.currentPlace) {
      //   const marker = {
      //     lat: this.currentPlace.geometry.location.lat(),
      //     lng: this.currentPlace.geometry.location.lng()
      //   }
      //   this.markers.push({ position: marker })
      //   this.places.push(this.currentPlace)
      //   this.center = marker
      //   this.currentPlace = null
      // }
    },
    geolocate: function () {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        }
      })
    },
    calculateAndDisplayRoute (directionsService, directionsDisplay) {
      directionsService.route({
        origin: {
        lat: 13.746909,
        lng: 100.539329
      },
        destination: {
        lat: 13.799274,
        lng: 100.550259
      },
        travelMode: 'DRIVING'
      }, function (response, status) {
        if (status === 'OK') {
          directionsDisplay.setDirections(response)
        } else {
          window.alert('Directions request failed due to ' + status)
        }
      })
    },
    displayRoute () {
      this.$gmapApiPromiseLazy().then( () => {
        // var map = new google.maps.Map();
        var start = new google.maps.LatLng(28.694004, 77.110291)
        var end = new google.maps.LatLng(28.72082, 77.107241)
        var directionsDisplay = new google.maps.DirectionsRenderer() // also, constructor can get "DirectionsRendererOptions" object
        directionsDisplay.setMap(document.getElementById('map')) // map should be already initialized.
        var request = {
          origin : start,
          destination : end,
          travelMode : google.maps.TravelMode.DRIVING
        }
        var directionsService = new google.maps.DirectionsService()
        directionsService.route(request, function(response, status) {
          if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
          }
        })
      })
    }
  },
  mounted () {
    // var landmarkRef = fire.database().ref().child('ตลาดน้ำตลิ่งชัน')
    // landmarkRef.on('value', (snapshot) => { this.detail = snapshot.val() })
    /* docRef.get().then((doc) => {
      var myData = doc.data()
      this.detail = myData.dd
    })
    //
    db.collection('landmark').get().then((querySnapshot) => {
      querySnapshot.forEach((doc) => {
      })
    }) */
    var ref = fire.database().ref('region/' + this.$route.params.regionName + '/' + this.$route.params.landmark)
    ref.on('value', (snapshot) => {
      this.center.lat = parseFloat(snapshot.val().lat)
      this.center.lng = parseFloat(snapshot.val().lng)
      this.detail = snapshot.val().detail
    })
    this.addMarker()
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
  width: 80%;
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
</style>
