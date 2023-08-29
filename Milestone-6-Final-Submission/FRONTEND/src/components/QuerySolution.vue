<template>
  <div class="flex-wrapper-five">
    <div class="flex-wrapper-eight">
      <div class="group-6">
        <img
          alt=""
          class="vector"
          src="https://static.overlay-tech.com/assets/d9b78edc-743d-4548-b31b-9b79b4c5a35b.svg"
        />
      </div>
      <p class="joe">{{ query.solved_by }}</p>
      <p class="course-instructor">~ Course Instructor</p>
      <img
        alt=""
        class="vector-two"
        src="https://static.overlay-tech.com/assets/7b6f5b15-0646-4191-ae20-1f75d4466956.svg"
      />
      <p class="solved-on-20-02-23-957-pm-ist">
        Solved on: {{ query.solved_at }}
      </p>
    </div>
    <p class="herein-the-recursive-function-will-call">
      {{ query.solution }}
    </p>
  </div>
</template>

<script>
export default {
  name: "QuerySolution",
  computed: {
    query() {
      return this.$store.getters.getSelectedQueries;
    },
  },
};
</script>

<style lang="scss" scoped>
.flex-wrapper-five {
  background-color: whitesmoke;
  margin: 50px;
  margin-bottom: 78px;
  border-radius: 5px;
  padding: 25px 39px 41px 49px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  border: 1px solid gainsboro;
}
.flex-wrapper-eight {
  margin-bottom: 45px;
  padding: 0 0 0 2px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.group-6 {
  background-color: #004b82;
  scale: 0.8;
  margin-right: 14px;
  border-radius: 50%;
  padding: 14px 12.5px 14.5px 13px;
  display: flex;
  align-items: center;
}
.vector {
  flex: 1;
  align-self: stretch;
  object-fit: cover;
}
.joe {
  color: black;
  text-align: center;
  margin-right: 24px;
  font-family: "Inter";
  font-size: 16px;
  font-weight: 500;
}
.course-instructor {
  font-family: "Inter";
  font-size: 16px;
  font-weight: 400;
  line-height: normal;
  color: rgba(103, 101, 101, 1);
  text-align: center;
  margin-right: 16px;
}
.vector-two {
  margin-right: 215px;
}
.solved-on-20-02-23-957-pm-ist {
  font-family: "Inter";
  font-size: 16px;
  font-weight: 400;
  line-height: normal;
  color: rgba(94, 94, 94, 1);
  text-align: center;
  margin-top: 1px;
}
.herein-the-recursive-function-will-call {
  color: black;
  align-self: stretch;
  display: flex;
  font-family: "Inter";
  font-size: 16px;
  font-weight: 500;
}
</style>
