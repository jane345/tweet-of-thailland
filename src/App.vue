<template>
  <div id="app" style="background-color: #7BA4DB">
  <!--<div id="app" style="background: url('http://f.ptcdn.info/484/006/000/1371921901-B02I1199-o.jpg') no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;background-size: cover;">-->
    <!-- <div class="ui inverted stackable menu">
      @click="gotoHome"
      <a class="item" ><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Flag_map_of_Thailand.svg/558px-Flag_map_of_Thailand.svg.png" style="width:35px; height:40px;"></a>
      <a class="item">Home</a>
    </div> -->
    <!-- <div class="ui inverted segment">
      <button class="tiny ui blue button"  style="margin-bottom: 5px; font-family: 'Caveat Brush', cursive; font-size: 1.25vw;" @click="$router.go(-1)"><i class="angle left icon"></i>Back</button>
      <button class="tiny ui blue button"  style="margin-bottom: 5px; font-family: 'Caveat Brush', cursive; font-size: 1.25vw;"  @click="gotoHome()"><i class="home icon"></i>Home</button>
    </div> -->
    <router-view/>
    <div class="ui inverted vertical footer segment">
      <!-- <button type="submit" @click="add()">Add Firebase</button> -->
    </div>
  </div>
</template>

<script>
// import GoogleMap from './components/GoogleMap'
export default {
  name: 'App',
  methods: {
    gotoHome () {
      this.$router.replace('/')
    },
    add () {
      this.$router.replace('/addja')
    }
  }
}
</script>

<style>
.ui.footer.segment {
  margin: 1em 0em 0em;
  padding: 1em 0em;
}
</style>
