<template>
  <div>
    <div class="query__list__box query__head__box">
      <p class="query__topic query__head">Topic</p>
      <p class="query__qn query__head">Query</p>
      <p class="query__priority query__head">Priority</p>
      <p class="query__status query__head">Status</p>
    </div>
    <QueryList v-for="(query, index) in queries" :query="query" :key="index" />
    <MakeAnnouncement v-if="announcementModal" />
    <CreatePostVue v-if="createPostModal" />
    <div class="add__query" @click="showmodal">+</div>
  </div>
</template>

<script>
import QueryList from "../components/QueryList.vue";
import CreatePostVue from "../components/CreatePost.vue";
import MakeAnnouncement from "../components/MakeAnnouncement.vue";
import axios from "axios";
export default {
  // eslint-disable-next-line
  name: "HomePage",
  components: {
    QueryList,
    CreatePostVue,
    MakeAnnouncement,
  },
  methods: {
    showmodal() {
      this.$store.state.createPostModal = !this.$store.state.createPostModal;
    },
    getQueries() {
      axios.get("/dashboard").then((res) => {
        console.log(res.data);
        this.$store.state.queries = res.data.queries;
        // console.log(this.queries);
      });
    },
  },
  created: function () {
    this.getQueries();
  },
  computed: {
    queries() {
      return this.$store.getters.getQueries;
    },
    announcementModal() {
      return this.$store.getters.getannoucementModal;
    },
    createPostModal() {
      return this.$store.getters.getCreatePostModal;
    },
  },
};
</script>

<style>
.query__head__box {
  background: linear-gradient(#026277, #004b82);
  margin: 50px;
  padding: 15px 25px;
  border-radius: 5px;
  border: 1px solid #004b82;
}
.query__head {
  color: #fff;
}
.query__list__box {
  display: flex;
  align-items: flex-start;
}
.add__query {
  color: #004b82;
  font-weight: bold;
  position: fixed;
  scale: 1.8;
  border: 2px solid #004b82;
  padding: 1px 5px;
  border-radius: 50%;
  right: 50px;
  bottom: 50px;
}
.add__query:hover {
  cursor: pointer;
}
</style>
