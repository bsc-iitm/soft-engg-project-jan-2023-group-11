<template>
  <div class="flex-wrapper-one">
    <p class="sir-can-you-please-explain-the-recursive">
      {{ query.query }}
    </p>
    <div class="flex-wrapper-seven">
      <p class="published-on-20-02-23-830-pm-ist">
        Published on : {{ query.created_at }}
      </p>
      <p class="num-2">&#43;{{ query.likes }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "QueryPost",
  computed: {
    query() {
      return this.$store.getters.getSelectedQueries;
    },
  },
};
</script>

<style lang="scss" scoped>
.flex-wrapper-one {
  background-color: whitesmoke;
  margin: 5px 50px;
  margin-bottom: 14px;
  border-radius: 5px;
  padding: 34px 44px 21px 47px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border: 1px solid gainsboro;
}
.sir-can-you-please-explain-the-recursive {
  height: 27.66%;
  color: black;
  align-self: stretch;
  margin-bottom: 20px;
  font-size: 18px;
  text-align: left;
  font-weight: 500;
}
.flex-wrapper-seven {
  display: flex;
  align-items: flex-start;
}
.published-on-20-02-23-830-pm-ist {
  width: 60%;
  height: 90.7%;
  font-family: "Inter";
  font-size: 16px;
  font-weight: 400;
  line-height: normal;
  color: rgba(94, 94, 94, 1);
  margin-top: 4px;
  margin-right: 535px;
}
.num-2 {
  width: 4%;
  height: 90.7%;
  color: black;
  font-size: 16px;
  font-weight: 500;
}
</style>
