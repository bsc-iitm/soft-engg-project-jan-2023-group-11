<template>
  <div class="bg">
    <img
      id="landing__image"
      src="../assets/landing_img.png"
      alt="landing image"
    />
    <div id="landing__text">
      <h2>Welcome To</h2>
      <div class="heading landing__heading">Quick Resolve</div>
      <button class="landing__login__btn" @click="pushToLogin">LOGIN</button>
      <p>New User?</p>
      <button class="landing__register__btn" @click="pushToRegister">
        REGISTER
      </button>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line
  name: "LandingPage",

  methods: {
    pushToLogin() {
      this.$router.push("/login");
    },
    pushToRegister() {
      this.$router.push("/register");
    },
  },
};
</script>
