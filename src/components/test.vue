<template>
<div>
<ul id="myList">
  <li>Coffee</li>
  <li>Tea</li>
</ul>
<button @click="myFunction()">Try it</button>
<button @click="clear()">Clear</button>
<img :src="'https://scontent.fbkk5-4.fna.fbcdn.net/v/t1.0-9/53030510_2176863352393822_2491574175529959424_n.jpg?_nc_cat=103&_nc_eui2=AeHM3Ib-1XWQ3LsnyCo7TVJ5tWTGv9xdUJr28kk3W4kyaqK9HWnHtcDJBaRzFY25jbjzt5X5N9sADx9sx6wb48Y9waa33K84tcEwRtTb87u0cA&_nc_ht=scontent.fbkk5-4.fna&oh=d9c19a0a51a9daa2e5e83c5b1797f8b8&oe=5D204875'">
</div>
</template>

<script>
export default {
  data () {
    return {
      array: ['Slide 1', 'Slide 2', 'Slide 3', 'Slide 4', 'Slide 5', 'Slide 6', 'Slide 7', 'Slide 8', 'Slide 9']
    }
  },
  methods: {
    listItem (item) {
      for (var i = 0; i < item.length; i++) {
        var list = item[i]
        console.log(list)
        list = document.createElement('li')
        document.getElementById('box').appendChild(list)
      }
    },
    myFunction () {
      var node = document.createElement('div')
      node.className = 'ui segment'
      var textnode = document.createTextNode('Water')
      node.appendChild(textnode)
      document.getElementById('myList').appendChild(node)
    },
    clear () {
      document.getElementById('myList').innerHTML = ''
    }
  },
  mounted () {}
}
</script>

<style>
.ui.celled.list {
    background-color: blue;
}

</style>
