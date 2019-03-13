<template>
  <div class="detail; ui raised segments; ui raised segment" style="margin:70px; border-color:#48C9B0; border-width:thick; background-color: rgba(0, 0, 0, 0.5);">
    
    
    <div align="right">
        <a class="ui blue inverted button" @click="gotoProfile">Profile</a>&emsp;
        <a class="ui yellow inverted button" @click="logout">Log out</a>
      </div>
      
       <div style="margin:10px 60px 60px 60px ">
          <h1 style="text-align:center; color:white" >{{placeFromUrl}}</h1>
        <div class="ui secondary teal inverted segment" style="padding:20px">
          <div class="ui piled segment">
            <div v-for="(detail,key) in details" :key='key'>
              <div v-for="(indetail,key) in detail.place" :key='key'>
                <div v-if="indetail.placename == placeFromUrl" >
                  <br>
                  <img :src="`/static/${indetail.image}`" width=100% height=50%>
                  <h1 style="text-align:center; color:#48C9B0">{{indetail.placename}}</h1>
                  <h4 style="text-align:center; color:teal">จังหวัด: {{indetail.province}}</h4>
                  <p>{{indetail.description}}</p>

                </div>
                
              </div>
            </div>
          </div>
        
        </div>

        <br>

        <div class="ui secondary teal inverted segment">
          
          
          <gmap-map :center="center" :zoom="12"  style="width:100%;  height: 400px;" >
          <gmap-marker :key="index" v-for="(m, index) in markers" :position="m.position" @click="center=m.position"> </gmap-marker>
          </gmap-map>
          
        </div>

        <br>

        

        <br>

        <!--<div class="ui secondary teal inverted segment" align="center">-->
        <div class="ui comments" style="text-align:left; margin:auto">
          <h3 class="ui dividing header" style="color: white;">Comments :</h3>
          <div class="comment" v-for="(detail,key) in details" :key='key'>
            <div v-for="(inusername,key) in detail.username" :key='key'>
              <!--<h1>{{detail.username}}</h1>-->
              <div v-if="inusername.placename == placeFromUrl" >
                <a class="avatar">
                <img src="http://webiconspng.com/wp-content/uploads/2017/09/Simpsons-PNG-Image-29703.png">
                </a>
                <div class="content">
                  <a class="author" style="color: white;">{{inusername.user}}</a>
                  <div class="metadata">
                    <div class="date" style="color: white;">{{inusername.datetime}}</div>
                  </div>
                  <div class="text">
                    <p style="color: white;">{{inusername.comment}}</p>
                  </div>
                </div>
              </div> 
            </div>
          </div>
          <form class="ui reply form">
            <div class="field">
              <textarea v-model="formData.comment" style="resize: none"></textarea>
            </div>
            <div class="ui primary submit labeled icon button" @click="addtext()">
              <i class="icon edit"></i> Add Comment
            </div>
          </form>
          </br>
          <div class="ui labeled button" tabindex="0">
            <div class="ui red button" type="button"  @click.once="heart++; addheart()">
              <i class="heart icon"></i> Like
            </div>
              <a class="ui basic red left pointing label">
                 {{heart}}
              </a>
          </div>
        </div>
        <!--</div>-->
        <br/><br/>
        <!--<router-link :to="{path: '/region/'+ regionBack}" style="margin:auto">-->
      
      
        
        <!--</router-link>-->
      </div>
      
       <div class="row" style="text-align:center;">
     <div class="ui animated fade button" tabindex="0" style="color:teal; width:100px;" @click="gobackRegion()">
          <div class="visible content"><i class="reply icon"></i></div>
          <div class="hidden content">
            Back
           
          </div>
        </div>
        </div>

  </div>
</template>

<script>
export default {
  name: 'detail',
  data () {
    return {
      msg: 'detail',
      detail: '',
      details: {},
      comment: "",
      placeFromUrl: "",
      regionBack:"",
      heart: 0,
      countI:0,
      countJ:0,
      countcomment:0,
      allcomments:{},
      comments:[],
      center: { lat: 15, lng: 70},
      markers: [],
      places: [],
      currentPlace: null,
      formData: {
              comment: '',
              datetime: '', // new Date().toDateString()
              placename: '',
              user: ''
          }
    }
  },
  
  mounted() {
   firebase.database().ref('6').on('value',(snapshot)=>{
        this.allcomments=snapshot.val()
      
    })
    
    this.countcomment = this.allcomments.username.length
   
  },
  created () {
  
    var i,j
    //console.log('start')
    firebase.database().ref().on('value', (snapshot) => {
      //console.log(snapshot.val())
      this.details = snapshot.val()
      this.placeFromUrl = this.$route.params.placename
      for(i=0; i<7; i++){
        for(j=0; j<10; j++){
          // alert(this.details[i].place[j].placename)
          // alert(this.$route.params.country)
          // alt(this.details[i].place[j].placename)
          if(this.details[i].place[j].placename === this.$route.params.placename){
            //alert(this.details[i].place[j].lat)
            //alert(this.details[i].place[j].lon)
            this.center.lat = this.details[i].place[j].lat
            this.center.lng = this.details[i].place[j].lon
            this.regionBack = this.details[i].regionname
            this.heart = this.details[i].place[j].heart
            this.countI = i
            this.countJ = j
            
            this.setPlace("สามพันโบก Lao Ngam, Pho Sai District, Ubon Ratchathani, Thailand")
          }
        }
      }
      this.geolocate();
      this.addMarker()
      
    })
    
  },
  methods:{
    setPlace: function(place) {
      this.currentPlace = place;
       //alert("setPlace",place)
    //console.log(place)
    this.addMarker()
    },
     addMarker: function() {
      if (true) {
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng()
        };
        this.markers.push({ position: marker });
        this.places.push(this.currentPlace);
        this.center = marker;
        this.currentPlace = null;
      }
     },
     geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
     },
     adddetail () {
      if(this.comment != ""){
        firebase.database().ref('details').push({comment: this.comment})
        .then((data) => {
          console.log(data)
        })
        .catch((error) => {
          console.log(error)
        })
        this.comment = ""
      }
    },
    gobackRegion(){
       this.$router.replace('/region/'+this.regionBack+'/'+this.$route.params.username)
       //console.log(this.details)
    },
    gotoProfile () {
       this.$router.replace('/profile/' + this.$route.params.username)
    },
    logout () {
      firebase.auth().signOut()
        .then(() => {
          this.$router.replace('/signin')
        })
        .catch((e) => {
          alert(e.message)
        })
    },
    addheart(userId, heart) {
            var postData = {
                  heart:this.heart,
            };
            
            var personRef = firebase.database().ref().child(this.countI).child("place").child(this.countJ);
          
            //console.log(personRef)
              personRef.once('value', function (snapshot) {
                if (snapshot.val() === null) {
                    alert('does not exist');
                } else {
                    personRef.update(postData);
                }
            });
    },
    
    addtext(){
          
        
            console.log(this.formData.comment)
            console.log(this.formData.datetime)
            console.log(this.formData.placename)
            console.log(this.formData.user)
            console.log(this.formData)
            this.formData.placename = this.$route.params.placename
            this.formData.user = this.$route.params.username
            this.formData.datetime = new Date().toString().slice(0,25)
            var personRef = firebase.database().ref().child(6).child("username").child(this.countcomment).set(this.formData);
            this.countcomment =  this.countcomment + 1
            this.comment = ""
            //console.log(personRef)
            this.formData.comment = ''
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
