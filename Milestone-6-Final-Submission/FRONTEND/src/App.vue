<template>
  <div>
    <!-- <h1>{{title}}</h1> -->
    <router-view />
    <!-- <input type="text" ref="name"/>
    <button @click="handleClick">click me</button>
    <ModalView header="sign up for goodies"/> -->
  </div>
</template>

<script>
// import ModalView from './components/ModalView.vue'

export default {
  name: "App",
  // components: { ModalView },
  //   data() {
  //     return{
  //       title: "Hello World :)"
  //     }
  //   },
  //   methods: {
  //     handleClick() {
  //       console.log(this.$refs.name)
  //       this.$refs.name.classList.add('active')
  //       this.$refs.name.focus()
  //     }
  //   }
};
</script>

<style>
#app {
  font-family: Inter;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
