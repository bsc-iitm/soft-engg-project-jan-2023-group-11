<template>
  <div class="box box__login">
    <h1 id="login__welcome">
      WELCOME <br />
      BACK
    </h1>
    <form @submit.prevent="login">
      <input type="text" placeholder="Username" v-model="user.userName" />
      <input
        type="password"
        placeholder="Password"
        v-model="user.userPassword"
      />
      <button id="login__btn">LOGIN</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "LoginBox",

  data() {
    return {
      user: {
        userName: "",
        userPassword: "",
      },
    };
  },

  methods: {
    login() {
      axios
        .get(`user/login/${this.user.userName}/${this.user.userPassword}`)
        .then((res) => {
          this.$router.push("/home");
          localStorage.user_id = res.data.user_id;
        })
        .catch((err) => {
          if (err.response.status === 404) {
            alert(
              `User with ${this.user.userName} username doesn't exist ! Please Register first`
            );
          }
          if (err.response.status === 401) {
            alert("Invalid Password !");
          }
          if (err.response.status === 500) {
            alert("Something went wrong ! Please Try Again");
          }
        });
    },
  },
};
</script>
