<template>
  <div>
    <div class="flex-wrapper-two">
      <p class="factorial-program">{{ query.title }}</p>
      <p class="author-jay-pritchett">{{ query.created_by }}</p>
      <p>{{ query.id }}</p>
    </div>
    <QueryPost />
    <QuerySolution v-if="query.solution" />
    <SolveQuery v-if="!query.solution" />
    <div class="flex-wrapper-six">
      <div class="flex-wrapper-four" @click="back">
        <img
          alt=""
          class="vector-three"
          src="https://static.overlay-tech.com/assets/5ec39976-c00c-4f86-8e1f-56de83bde7d1.svg"
        />
        <p class="back">BACK</p>
      </div>
      <div class="flex-wrapper-three">
        <img
          alt=""
          class="vector-four"
          src="https://static.overlay-tech.com/assets/d6fe2576-5620-4152-882a-1622d1b1951a.svg"
        />
        <p class="pin-query">PIN QUERY</p>
      </div>
    </div>
    <ReplyPost v-if="replyModal" />
  </div>
</template>

<script>
import QueryPost from "../components/QueryPost.vue";
import QuerySolution from "../components/QuerySolution.vue";
import SolveQuery from "../components/SolveQuery.vue";
import ReplyPost from "../components/ReplyPost.vue";

export default {
  name: "QueryViewPage",
  components: { QueryPost, QuerySolution, SolveQuery, ReplyPost },
  methods: {
    back() {
      this.$router.push("/home");
    },
  },
  computed: {
    query() {
      return this.$store.getters.getSelectedQueries;
    },
    replyModal() {
      return this.$store.getters.getreplyPostModal;
    },
  },
};
</script>

<style lang="scss" scoped>
.flex-wrapper-two {
  margin-bottom: 23px;
  margin-left: 1px;
  margin: 50px;
  border-radius: 5px;
  padding: 22px 34px 21px 47px;
  display: flex;
  align-items: center;
  border: 2px solid #026277;
}
.factorial-program {
  width: 24.23%;
  color: black;
  align-self: stretch;
  text-align: center;
  margin-right: 527px;
  font-size: 24px;
  font-weight: 600;
}
.author-jay-pritchett {
  width: 29.18%;
  color: grey;
  align-self: stretch;
  text-align: center;
  font-size: 24px;
  font-weight: 400;
}
.flex-wrapper-six {
  padding: 0 0 0 1px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.flex-wrapper-four {
  background-color: #004b82;
  margin-right: 690px;
  border-radius: 10px;
  padding: 16px 77px 16px 49px;
  display: flex;
  align-items: center;
}
.vector-three {
  width: 17.52%;
  height: 66.67%;
  margin-right: 28px;
}
.back {
  // width: 62.04%;
  font-family: "Inter";
  font-size: 18px;
  font-weight: 700;
  line-height: normal;
  color: whitesmoke;
  align-self: stretch;
  text-align: center;
}
.flex-wrapper-four:hover {
  cursor: pointer;
}
.flex-wrapper-three {
  background-color: #004b82;
  border-radius: 10px;
  padding: 16px 25px 16px 27px;
  display: flex;
  align-items: center;
}
.vector-four {
  width: 11.37%;
  height: 88.89%;
  margin-right: 25px;
}
.pin-query {
  // width: 76.78%;
  font-family: "Inter";
  font-size: 18px;
  font-weight: 700;
  line-height: normal;
  color: whitesmoke;
  align-self: stretch;
  text-align: center;
}
</style>
