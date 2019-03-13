<template>
  <div class="home">
    <div class="ui raise segment">
      <h1 class="ui block header"><i class="plane icon"></i>Tweet Of Thailand</h1>
      <br>
      <div class="ui three link cards" style="margin: auto;">
        <div class="card" v-for="(region,index) in regionName" :key="index" >
          <div class="image"  @click="gotoRegion(region)">
            <img :src="'/static/' + region + '.jpeg'">
          </div>
          <div class="content"  @click="gotoRegion(region)">
          <div class="header" style="text-align:center; font-family: 'Athiti', sans-serif; font-weight: 1.75vm;">{{region}}</div>
          </div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
import {fire} from './firebase'
var ref = fire.database().ref('region')
export default {
  data () {
    return {
      regionName: []
    }
  },
  methods: {
    gotoRegion (regionName) {
      this.$router.push({ path: `/${regionName}/` })
      // this.$router.replace('/' + regionName + '/')
    }
  },
  mounted () {
    /* ---------------------------read from firestore --------------------------
    db.collection('landmark').get().then((querySnapshot) => {
      querySnapshot.forEach(doc => {
        this.regionName.push(doc.id)
      })
    }) */
    // ---------------------------read from firebase -----------------------------
    ref.on('value', (snapshot) => {
      snapshot.forEach((childSnapshot) => {
        // var childKey = childSnapshot.key
        // var childData = childSnapshot.val()
        this.regionName.push(childSnapshot.key)
      })
    })
  }
}
</script>

<style>
.cards {
  width: 90%;
  font-size: 80%;
}
.ui.raise.segment {
  margin:auto;
  width: 95%;
  border-color:#27549E;
  border-width: thick;
  background-color: rgba(0, 0, 0, 0.5);
}
.ui.block.header{
  width: 80%;
  margin: auto;
  font-family: 'Caveat Brush', cursive ,'Athiti', sans-serif;
  text-align:center;
  color:white;
  background-color:#27549E;
}
</style>
