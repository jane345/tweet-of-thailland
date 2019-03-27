<template>
  <div class="region">
    <select id="op">
      <option value="ภาคกลาง">ภาคกลาง</option>
      <option value="ภาคเหนือ">ภาคเหนือ</option>
      <option value="ภาคใต้">ภาคใต้</option>
      <option value="ภาคตะวันออก">ภาคตะวันออก</option>
      <option value="ภาคตะวันออกเฉียงเหนือ">ภาคตะวันออกเฉียงเหนือ</option>
      <option value="ภาคตะวันตก">ภาคตะวันตก</option>
    </select>
    <button type="submit" @click="select()">Select</button>
    <div id="Select_Landmark"></div>
    <br>
    <br>
    <textarea rows="10" cols="30" id="DetailLandMark" placeholder="detail"></textarea>
    <input type="text" id="lat" placeholder="lat">
    <input type="text" id="lng" placeholder="lng">
    <input type="text" id="src" placeholder="link cover img">
    <br>
    <input type="text" id="no" placeholder="no">
    <input type="text" id="url_img" placeholder="link url img">
    <input type="text" id="url_twitter" placeholder="link url twitter">
    <button type="submit" @click="addDetail()">Update</button>
      <br>
      <br>
    <input type="text" id="old" placeholder="Old">
    <input type="text" id="new" placeholder="New">
    <button type="submit" @click="edit">Edit</button>
  </div>
</template>

<script>
import {fire} from './firebase'
var ref = fire.database().ref('region')
export default {
  data () {
    return {
      LandMark: []
    }
  },
  methods: {
    // addtodB () {
    //   // ------ add to firestore
    //   /* var regionRef = db.doc('/landmark/' + this.$route.params.region)
    //   const LandMarkInput = document.getElementById('text').value
    //   var LandMarkDetail = document.getElementById('value').value
    //   regionRef.update({
    //     [LandMarkInput]: LandMarkDetail
    //   }) */
    //   // ==========================================================================================
    //   // ------ add to firebase ยังไม่เช็คชื่อซ้ำ
    //   var reIn = document.getElementById('Region').value
    //   var nameIn = document.getElementById('NameLandMark').value
    //   var valIn = document.getElementById('ValueLandMark').value
    //   if (reIn !== '') {
    //     ref.push(reIn)
    //   }
    //   var reRef = ref.child('ภาคตะวันออก')
    //   reRef.update({[nameIn]: valIn})
    //   console.log(nameIn)
    // },
    select () {
      var e = document.getElementById('op')
      var reg = e.options[e.selectedIndex].value
      var landmarkRef = ref.child(reg)
      landmarkRef.on('value', (snapshot) => {
        snapshot.forEach((childSnapshot) => {
          this.LandMark.push(childSnapshot.key)
          // console.log(childSnapshot.key)
        })
      })
      var myDiv = document.getElementById('Select_Landmark')
      myDiv.innerHTML = ''
      var array = this.LandMark
      var selectList = document.createElement('select')
      selectList.id = 'mySelect'
      myDiv.appendChild(selectList)
      for (var i = 0; i < array.length; i++) {
        // var selectList = document.createElement('select')
        // selectList.id = 'Select_Landmark'
        var option = document.createElement('option')
        option.value = array[i]
        option.text = array[i]
        selectList.appendChild(option)
      }
    },
    addDetail () {
      var x = document.getElementById('mySelect')
      var LM = x.options[x.selectedIndex].value
      // var LM = document.getElementById('NameLandMark').value
      var det = document.getElementById('DetailLandMark').value
      var lat = document.getElementById('lat').value
      var lng = document.getElementById('lng').value
      var src = document.getElementById('src').value
      var e = document.getElementById('op')
      var reg = e.options[e.selectedIndex].value
      var reRef = ref.child(reg + '/' + LM)
      if (det !== '') { reRef.update({'detail': det}) }
      if (lat !== '') { reRef.update({'lat': lat}) }
      if (lng !== '') { reRef.update({'lng': lng}) }
      if (src !== '') { reRef.update({'src': src}) }
      var url = document.getElementById('url_img').value
      var twitter = document.getElementById('url_twitter').value
      var no = document.getElementById('no').value
      if (url !== '') { reRef.child('/url').update({[no]: url}) }
      if (twitter !== '') { reRef.child('/twitter').update({[no]: twitter}) }
      alert('updated successfully!')
    },
    edit () {
      var e = document.getElementById('op')
      var reg = e.options[e.selectedIndex].value
      var oldName = document.getElementById('old').value
      var newName = document.getElementById('new').value
      var reRefOld = ref.child(reg + '/' + oldName)
      var reRefNew = ref.child(reg + '/' + newName)
      var Edit = {}
      reRefOld.on('value', (snapshot) => {
        Edit = snapshot.val()
      })
      reRefNew.set(Edit)
      console.log(Edit)
      // reRefOld.remove()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style>
</style>
