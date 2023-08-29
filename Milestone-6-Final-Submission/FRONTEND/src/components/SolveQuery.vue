<template>
  <div class="component-3">
    <p class="this-query-hasnt-been-solved-yet">
      This query hasn&#039;t been solved yet!
    </p>
    <div class="flex-wrapper-one" @click="replyPostMethod">
      <div class="group-13">
        <img
          alt=""
          class="vector"
          src="https://static.overlay-tech.com/assets/0c3dcaf0-19be-48ae-8691-35aa606df437.svg"
        />
        <p class="add-a-solution">Add a Solution</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SolveQuery",

  methods: {
    replyPostMethod() {
      console.log(this.$store.state.replyPostModal);
      this.$store.state.replyPostModal = !this.$store.state.replyPostModal;
    },
  },
};
</script>

<style lang="scss" scoped>
.component-3 {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.this-query-hasnt-been-solved-yet {
  height: 28.13%;
  font-family: "Inter";
  font-size: 24px;
  font-weight: 600;
  line-height: normal;
  color: rgb(37, 37, 37);
  align-self: stretch;
  margin-top: 60px;
  margin-bottom: 30px;
}
.flex-wrapper-one {
  background-color: #024351;
  border-radius: 10px;
  padding: 21px 43px;
  display: flex;
  align-items: center;
}

.flex-wrapper-one:hover {
  cursor: pointer;
}
.group-13 {
  display: flex;
  align-items: center;
}
.vector {
  width: 10.22%;
  height: 66.67%;
  margin-right: 33px;
}
.add-a-solution {
  width: 77.74%;
  font-family: "Inter";
  font-size: 18px;
  font-weight: 700;
  line-height: normal;
  color: whitesmoke;
  align-self: stretch;
  text-align: center;
}
</style>
