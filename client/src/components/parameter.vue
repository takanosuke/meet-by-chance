<template>
    
</template>
        <!-- 折りたたみボタン -->
        <b-button variant=outline-dark v-b-toggle.collapse class="mt-2 my-1 px-5">Parameters</b-button>
        <!-- パラメータ -->
        <b-collapse id="collapse">
          <b-row>
            <b-col sm="2"></b-col>
            <b-col sm="1">
              <label>Density:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input type="range" min="1" max="100" v-model="density"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="density=50">Reset</b-btn>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="2"></b-col>
            <b-col sm="1">
              <label>Color:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input type="range" min="1" max="100" v-model="color"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="color=50">Reset</b-btn>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="2"></b-col>
            <b-col sm="1">
              <label>Visibility:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input type="range" min="1" max="100" v-model="visibility"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="visibility=50">Reset</b-btn>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="2"></b-col>
            <b-col sm="1">
              <label>Blurry:</label>
            </b-col>
            <b-col sm="6">
              <b-form-input type="range" min="1" max="100" v-model="blurry"></b-form-input>
            </b-col>
            <b-col sm="3">
              <b-btn size="sm" v-on:click="blurry=50">Reset</b-btn>
            </b-col>
          </b-row>
        </b-collapse>
    
