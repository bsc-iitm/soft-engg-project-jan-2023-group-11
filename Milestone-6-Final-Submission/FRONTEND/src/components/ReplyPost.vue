<template>
  <div class="component-6">
    <form>
      <div class="query">
        <label>Query Title</label>
        <br />
        <p>{{ query.query }}</p>
        <br /><br />
        <label>Query Solution</label><br />
        <textarea
          rows="5"
          cols="80"
          placeholder="Type your query here...."
          v-model="solution"
        ></textarea>
        <br />
      </div>
    </form>
    <div class="flex-wrapper-three">
      <div class="group-14" @click="postQuery">
        <p class="post">POST</p>
        <img
          alt=""
          class="vector-two"
          src="https://static.overlay-tech.com/assets/40f3b71c-c6e0-4b5d-adb4-ac80d7d7fd78.svg"
        />
      </div>
    </div>
    <div class="flex-wrapper-one">
      <p class="post-a-query">{{ query.title }}</p>
      <div class="minus">
        <div class="vector-three"></div>
      </div>
      <div class="window-restore">
        <img
          alt=""
          class="vector-five"
          src="https://static.overlay-tech.com/assets/93c533fa-cf82-4ca2-bf1b-fea59860f749.svg"
        />
      </div>
      <div class="window-close" @click="closemodal">
        <img
          alt=""
          class="vector-four"
          src="https://static.overlay-tech.com/assets/3f69b841-100f-410b-b251-62ab7da2a072.svg"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CreatePost",
  data() {
    return {
      solution: "",
    };
  },
  methods: {
    postQuery() {
      const userID = localStorage.user_id;
      const queryId = this.$store.getters.getSelectedQueries.id;
      console.log(queryId);
      axios
        .put(`/support_staff/${userID}/resolve/${queryId}/${this.solution}`)
        .then((res) => {
          console.log(res);
          this.$store.state.queries = res.data.queries;
          this.$store.state.replyPostModal = !this.$store.state.replyPostModal;
          this.$router.push("/home");
        })
        .catch((err) => {
          // console.log(err);
        });
    },
    closemodal() {
      // console.log(12);
      this.$store.state.replyPostModal = !this.$store.state.replyPostModal;
    },
  },

  computed: {
    query() {
      return this.$store.getters.getSelectedQueries;
    },
  },
};
</script>

<style lang="scss" scoped>
.component-6 {
  position: fixed;
  background-color: whitesmoke;
  right: -50px;
  bottom: 5px;
  margin: 50px 400px 20px 20px;
  border-radius: 10px;
  padding: 124px 24px 22px 51px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border: 1px solid #026277;
}
.flex-wrapper-two {
  background-color: white;
  margin-bottom: 48px;
  border-radius: 10px;
  padding: 11px 33px 10px 49px;
  display: flex;
  align-items: center;
  border: 1px solid gainsboro;
}
.python {
  font-family: "Inter";
  font-size: 16px;
  font-weight: 600;
  line-height: normal;
  color: #026277;
  align-self: stretch;
  text-align: center;
  margin-right: 165px;
}

#category {
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
}

.query {
  border: 1px solid gainsboro;
  border-radius: 5px;
  padding: 20px;
  text-align: left;
  font-size: 18px;
}

textarea {
  border: 1px solid gainsboro;
  margin-top: 8px;
  padding: 5px;
  border-radius: 5px;
  font-size: 14px;
  font-family: "Inter";
  background: #e7e7e7;
}

textarea:hover {
  cursor: pointer;
}

.flex-wrapper-three {
  background-color: #026277;
  margin-left: 713px;
  border-radius: 10px;
  padding: 23px 31px 23px 48px;
  display: flex;
  align-items: center;
}
.group-14 {
  display: flex;
  align-items: center;
}

.group-14:hover {
  cursor: pointer;
}
.post {
  width: 37.31%;
  font-family: "Inter";
  font-size: 18px;
  font-weight: 700;
  line-height: normal;
  color: whitesmoke;
  align-self: stretch;
  text-align: center;
  margin-right: 60px;
}

.vector-two {
  width: 17.91%;
  height: 95.45%;
}
.flex-wrapper-one {
  background-color: #026277;
  width: 91%;
  border-radius: 10px 10px 0px 0px;
  padding: 29px 23px 29px 67px;
  display: flex;
  align-items: center;
  position: absolute;
  left: -1px;
  top: -1px;
  border: 2px solid #026277;
}

.post-a-query {
  width: 16.39%;
  height: 91.67%;
  font-family: "Inter";
  font-size: 18px;
  font-weight: 600;
  line-height: normal;
  color: white;
  margin-right: 624px;
}
.minus {
  width: calc(2.64% - 10px);
  margin-right: 32px;
  padding: 11px 5px;
  display: flex;
  align-items: center;
  align-self: stretch;
}
.vector-three {
  background-color: white;
  flex: 1;
  align-self: stretch;
}
.window-restore {
  width: calc(2.56% - 8px);
  height: calc(61.54% - 8px);
  margin-top: 5px;
  margin-right: 15px;
  padding: 4px;
  display: flex;
  align-items: center;
}
.vector-four {
  flex: 1;
  align-self: stretch;
  object-fit: cover;
}
.window-close {
  width: calc(2.64% - 10px);
  padding: 5px;
  display: flex;
  align-items: center;
  align-self: stretch;
}
</style>
