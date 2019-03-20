<template>
  <div class="region">
    <div class="ui inverted segment">
      <button class="tiny ui blue button"  style="margin-bottom: 5px; font-family: 'Caveat Brush', cursive; font-size: 1.25vw;" @click="$router.go(-1)"><i class="angle left icon"></i>Back</button>
      <button class="tiny ui blue button"  style="margin-bottom: 5px; font-family: 'Caveat Brush', cursive; font-size: 1.25vw;"  @click="gotoHome()"><i class="home icon"></i>Home</button>
  </div>
      <!-- <div class="ui raise segment" style="margin:50px; border-color:#27549E; padding:10px;  border-width: thick; background-color: rgba(0, 0, 0, 0.5);"> -->
      <h1 class="ui block header" > {{$route.params.region}} </h1>
      <!-- </div> -->
      <br>
      <div class="ui three link cards" style="margin: auto;">
        <div class="ui card" v-for="(landmark,index) in LandMark" :key="index" >
          <div class="image"  @click="gotoDetail(landmark)">
            <img :src="Src[index]">
          </div>
          <div class="content"  @click="gotoDetail(landmark)">
            <div class="header" style="text-align:center; font-family: 'Athiti', sans-serif; font-weight: 1.75vm;">{{landmark}}</div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import {fire} from './firebase'
export default {
  data () {
    return {
      LandMark: [],
      Src: []
    }
  },
  methods: {
    gotoHome () {
      this.$router.replace('/')
    },
    gotoDetail (LandMark) {
      this.$router.push({ path: `${this.$route.path}${LandMark}/` })
    }
  },
  mounted () {
    /*
    db.doc('/landmark/' + this.$route.params.region).get().then((doc) => {
      var x = doc.data()
      Object.keys(x).forEach(function (keyy) {
        field.push(keyy)
      })
    })
    */
    // ref = ref.child(this.$route.params.region)
    var landmarkRef = fire.database().ref().child('/region/' + this.$route.params.region)
    landmarkRef.on('value', (snapshot) => {
      snapshot.forEach((childSnapshot) => {
        this.LandMark.push(childSnapshot.key)
        this.Src.push(childSnapshot.val().src)
      })
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style>
.ui.top.attached.header{
  font-family: 'Caveat Brush', cursive ,'Athiti', sans-serif;
  text-align:center;
  color:white;
  background-color:#27549E;
}
.ui.block.header{
  width: 90%;
  margin: auto;
  font-family: 'Caveat Brush', cursive ,'Athiti', sans-serif;
  text-align:center;
  color:white;
  background-color:#27549E;
}
.cards {
  width: 85%;
  font-size: 80%;
}
.image {
   overflow: hidden;
   position: relative;
   height: 250px;
}

.image img {
   max-width: 100%;
   min-height: 100%;
   min-width: 100%;
   object-fit: cover;
}
</style>
