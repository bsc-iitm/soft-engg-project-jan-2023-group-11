<template>
  <div>
    <div class="query__list__boxes" @click="viewQueryPage">
      <div class="query__list__box">
        <p class="query__topic">{{ query.category }}</p>
        <p class="query__qn">{{ query.title }}</p>
        <p class="query__priority">{{ query.likes }}</p>
        <p class="query__status">{{ query.status }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "QueryList",
  props: ["query"],
  data() {
    return {
      showfullquery: false,
    };
  },
  methods: {
    viewQueryPage() {
      this.$router.push("/query");
      this.$store.state.selectedQuery = this.query;
    },
  },
};
</script>

<style lang="scss">
.query__list__boxes {
  background-color: whitesmoke;
  margin: 50px;
  margin-bottom: 23px;
  border-radius: 5px;
  padding: 23px 51px 22px 59px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  border: 1px solid gainsboro;
}

.query__list__boxes:hover {
  cursor: pointer;
}

.query__list__box {
  display: flex;
  align-items: flex-start;
}
.query__topic {
  width: 10.05%;
  color: black;
  align-self: stretch;
  text-align: center;
  margin-right: 177px;
  font-size: 16px;
  font-weight: 500;
  font-family: "Inter";
  // @include inter-32-semi-bold;
}
.query__qn {
  width: 14.86%;
  color: black;
  align-self: stretch;
  text-align: center;
  margin-right: 227px;
  font-size: 16px;
  font-weight: 500;
  // @include inter-32-semi-bold;
}
.query__priority {
  width: 3.71%;
  color: black;
  align-self: stretch;
  text-align: center;
  margin-right: 238px;
  font-size: 16px;
  font-weight: 500;
  // @include inter-32-semi-bold;
}
.query__status {
  width: 13.22%;
  color: black;
  align-self: stretch;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  // @include inter-32-semi-bold;
}
</style>
