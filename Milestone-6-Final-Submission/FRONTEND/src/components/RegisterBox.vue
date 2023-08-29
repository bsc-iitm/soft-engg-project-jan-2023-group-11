<template>
  <div class="box">
    <h1>
      REGISTER <br />
      NOW
    </h1>
    <form @submit.prevent="register">
      <input type="text" placeholder="Username" v-model="user.userName" />
      <input
        type="password"
        placeholder="Password"
        v-model="user.userPassword"
      />
      <div id="register__radios">
        <label class="register__radio"
          ><input
            type="radio"
            checked="checked"
            value="STUDENT"
            v-model="user.userType"
          />Student</label
        ><br />
        <label class="register__radio"
          ><input
            type="radio"
            value="SUPPORT_STAFF"
            v-model="user.userType"
          />Course Instructor</label
        ><br />
        <label class="register__radio"
          ><input
            type="radio"
            value="ADMIN"
            v-model="user.userType"
          />Admin</label
        >
      </div>
      <button id="register__btn">REGISTER</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "RegisterBox",

  data() {
    return {
      user: {
        userName: "",
        userPassword: "",
        userType: "STUDENT",
      },
    };
  },

  methods: {
    register() {
      console.log(this.user.userType);

      axios
        .post(
          `/user/adduser/${this.user.userName}/${this.user.userPassword}/${this.user.userType}`
        )
        .then((res) => {
          this.$router.push("/login");
        })
        .catch((err) => {
          if (err.response.status === 409) {
            alert(
              "User with same username already exist ! Please Choose a different username"
            );
            (this.user.userName = ""), (this.user.userPassword = "");
          } else {
            alert("Something went wrong ! Please Try Again");
          }
        });
    },
  },
};
</script>
