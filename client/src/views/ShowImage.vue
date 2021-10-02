<template>
  <b-container>
    <!-- 画面上部 -->
    <div class="text-center my-5">
      <div v-if="loading">
        <h3>Creating...</h3>
        <b-spinner variant="primary" label="Creating..."></b-spinner>
      </div>
      <div v-else>
        <b-button size="lg" id="resultImage" variant="primary" v-on:click="runCreate">{{CreateBtnText}}</b-button>
        <b-button size="lg" v-b-toggle.parameter-sidebar>Parameter</b-button>
      </div>
    </div>
    <!-- 画面下部 -->
    <div>
      <b-tabs>
        <b-tab v-for="f in frameList" :key="'tab-' + f.text" :title="f.text" v-on:click="changeFrame(f.value)"></b-tab>
          <!-- 表示する画像 -->
          <b-img class="mt-3 mb-3" :center="true" :src="imageUrl" v-if="created" />
          <div class="text-center my-4" v-else><h3>Please push "Create" button.</h3></div>
          <!-- <h5>{{ imageName }}</h5> -->
          <!-- <a :href="imageUrl" download><b-button>Detail</b-button></a> -->
        <!-- New Tab Button (Using tabs-end slot) -->
        <template #tabs-end>
          <b-nav-item role="presentation" @click.prevent="newTab" href="#"><b>+</b></b-nav-item>
        </template>
      </b-tabs>
    </div>
    <!-- その他 -->
    <div>
      <!-- パラメータサイドバー -->
      <b-sidebar id="parameter-sidebar" title="Parameter" left shadow>
        <div class="px-3 py-2">

          <label>Density:</label>
          <b-row>
            <b-col sm="9">
              <b-form-input type="range" min="1" max="100" v-model="density"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="density=50">Reset</b-btn>
            </b-col>
          </b-row>

          <label>Color:</label>
          <b-row>
            <b-col sm="9">
              <b-form-input type="range" min="1" max="100" v-model="color"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="color=50">Reset</b-btn>
            </b-col>
          </b-row>

          <label>Visibility:</label>
          <b-row>
            <b-col sm="9">
              <b-form-input type="range" min="1" max="100" v-model="visibility"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="visibility=50">Reset</b-btn>
            </b-col>
          </b-row>

          <label>Blurry:</label>
          <b-row>
            <b-col sm="9">
              <b-form-input type="range" min="1" max="100" v-model="blurry"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="blurry=50">Reset</b-btn>
            </b-col>
          </b-row>

          <label>Shift:</label>
          <b-row>
            <b-col sm="9">
              <b-form-input type="range" min="1" max="100" v-model="shift"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="shift=50">Reset</b-btn>
            </b-col>
          </b-row>
        </div>
      </b-sidebar>
    </div>
  </b-container>
</template>

<script>
import axios from 'axios';
// import ParameterSidebar from './ParameterSidebar';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
export default {
  // components: {
  //   ParameterSidebar
  // },
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
      if (this.created)
        this.deleteImage()
      await this.fetchImage()
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
