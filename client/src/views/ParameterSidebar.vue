<template>
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
</template>

<script>
export default {
    data(){
        return {
          name: 'ParameterSidebar'
        }
    }
}
</script>