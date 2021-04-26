<template>
  <div>
    <div class="random">
      <h1>This is a random page</h1>
      <p>ルーレット：{{random_number}}</p>
      <el-button type="primary" round @click="getData">Start</el-button>
    </div>
  </div>
</template>

<!--region script-->
<script>
import axios from 'axios'
import {API_BASE_URI} from '../../util/const.js'

export default {
  name: 'random',
  data() {
    return {
      random_number: 0,
    };
  },
  methods: {
    getData () {
      const path = API_BASE_URI + '/rand'
      axios.get(path)
          .then(response => {
            console.log(response)
            this.random_number= response.data.randomNum;
          })
          .catch(error => {
          console.log(error)
          })
    },
  }
}
</script>

<style>  
.swagger_test {
  padding-top: 100px;
}
</style>