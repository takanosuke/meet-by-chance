<template>
  <b-container>
    <div class="text-center my-5">
      <div v-if="loading">
        <h3>Creating...</h3>
        <b-spinner variant="primary" label="Creating..."></b-spinner>
      </div>
      <div v-else>
        <b-button size="lg" id="resultImage" variant="primary" v-on:click="runCreate">{{CreateBtnText}}</b-button>
        <b-button size="lg" v-b-toggle.parameter-sidebar>Parameter</b-button>
        <ParameterSidebar></ParameterSidebar>
      </div>
    </div>
    <div>
      <b-tabs>
        <b-tab v-for="f in frameList" :key="'tab-' + f.text" :title="f.text" v-on:click="changeFrame(f.value)"></b-tab>
          <!-- 表示する画像 -->
          <b-img class="mt-3 mb-3" :center="true" :src="imageUrl" v-if="created" />
          <div class="text-center my-4" v-else>Please push "Create" button.</div>
          <!-- <h5>{{ imageName }}</h5> -->
          <!-- <a :href="imageUrl" download><b-button>Detail</b-button></a> -->
      </b-tabs>
    </div>
  </b-container>
</template>

<script>
import axios from 'axios';
import ParameterSidebar from './ParameterSidebar';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
export default {
  components: {
    ParameterSidebar
  },
  name: 'ShowImage',
  data () {
    return {
      CreateBtnText: 'Create',
      imageUrl: '',
      imageName: 'Welcome!',
      density: 50,
      visibility: 50,
      blurry: 50,
      shift: 50,
      color: 50,
      frame: 'rectangle.png',
      frameList: [
        { text: 'Rectangle', value: 'rectangle.png' },
        { text: 'Shoes', value: 'shoes.png' },
        { text: 'T-shirt', value: 't-shirt.png'},
        { text: 'Draemon', value: 'draemon.png'}],
      loading: false,
      created: false
      
    }
  },
  created() {
  },
  methods: {
    async runCreate() {
      this.loading = true
      this.CreateBtnText='Re Create'
      await this.fetchImage()
      if (this.created)
        this.deleteImage()
      this.loading = false
      this.created = true
    },
    async fetchImage () {
      await axios
      .post('http://127.0.0.1:8000/image/create/', {
        density: this.density,
        visibility: this.visibility,
        color: this.color,
        blurry: this.blurry,
        shift: this.shift,
        frame: this.frame
      })
      .then(res => {
        this.imageUrl = res.data.url
        this.imageName = res.data.name
      })
      .catch(res => {console.log(res)})
    },
    async changeFrame (frame_name) {
      this.frame = frame_name
      if (this.created){
        await axios
        .post('http://127.0.0.1:8000/image/changeframe/', {
          img_name: this.imageName,
          frame: frame_name
        })
        .then(res => {
          this.imageUrl = res.data.url
          this.imageName = res.data.name
        })
        .catch(res => {console.log(res)})
      }
    },
    deleteImage () {
      axios
      .delete(`http://127.0.0.1:8000/image/delete/${this.imageName}/`,{})
      .then(res => {console.log(res)})
      .catch(res => {console.log(res)})
    }
  },
}
</script>
