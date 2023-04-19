<template>
  <div class="component-1">
    <div class="flex-wrapper-five">
      <div class="group-7">
        <div class="group-6">
          <img
            alt=""
            class="vector"
            src="https://static.overlay-tech.com/assets/8f90ad57-5402-4780-9daf-f4e45ce5c34d.svg"
          />
        </div>
        <p class="joe">Joe</p>
      </div>
      <img
        alt=""
        class="vector-two"
        src="https://static.overlay-tech.com/assets/3e4da78e-0f8e-472e-911b-685f8320667f.svg"
      />
    </div>
    <div class="flex-wrapper-one">
      <div class="group-9">
        <p class="topic">Topic</p>
        <p class="query">Query</p>
        <p class="priority">Priority</p>
        <p class="status">Status</p>
      </div>
    </div>
    <div class="flex-wrapper-two">
      <div class="group-9">
        <p class="python">Python</p>
        <p class="week-4-q1">Week 4 Q1</p>
        <p class="num-2">&#43;2</p>
        <p class="unsolved">Unsolved</p>
      </div>
    </div>
    <div class="flex-wrapper-three">
      <div class="group-9">
        <p class="soft-engg">Soft. Engg</p>
        <p class="quiz-1-syllabus">Quiz 1 Syllabus</p>
        <p class="num-1">&#43;1</p>
        <p class="solved">Solved</p>
      </div>
    </div>
    <div class="flex-wrapper-four">
      <div class="group-9">
        <p class="python-two">Python</p>
        <p class="factorial-program">Factorial program</p>
        <p class="num-2-two">&#43;2</p>
        <p class="solved-two">Solved</p>
      </div>
    </div>
    <img
      alt=""
      class="vector-three"
      src="https://static.overlay-tech.com/assets/1ea90afd-dc27-4cd2-9e26-c11617ec5817.svg"
    />
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line
  name: "Component1",
};
</script>

<style lang="scss" scoped>
.component-1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.flex-wrapper-five {
  margin-bottom: 98px;
  display: flex;
  align-items: center;
}
.group-7 {
  margin-right: 993px;
  display: flex;
  align-items: center;
}
.group-6 {
  background-color: $teal-2;
  margin-right: 35px;
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
  width: 50.29%;
  color: $teal;
  align-self: stretch;
  text-align: center;
  @include inter-48-bold;
}
.vector-two {
  width: 2.02%;
  height: 41.38%;
}
.flex-wrapper-one {
  background-color: $teal;
  margin-bottom: 23px;
  margin-left: 1px;
  border-radius: 5px;
  padding: 24px 73px 23px 74px;
  display: flex;
  align-items: center;
}
.group-9 {
  display: flex;
  align-items: flex-start;
}
.topic {
  width: 7.95%;
  color: $white;
  align-self: stretch;
  text-align: center;
  margin-right: 225px;
  @include inter-32-semi-bold;
}
.query {
  width: 8.89%;
  color: $white;
  align-self: stretch;
  text-align: center;
  margin-right: 225px;
  @include inter-32-semi-bold;
}
.priority {
  width: 10.57%;
  color: $white;
  align-self: stretch;
  text-align: center;
  margin-right: 225px;
  @include inter-32-semi-bold;
}
.status {
  width: 9.45%;
  color: $white;
  align-self: stretch;
  text-align: center;
  @include inter-32-semi-bold;
}
.flex-wrapper-two {
  background-color: $white-smoke;
  margin-bottom: 23px;
  border-radius: 5px;
  padding: 23px 51px 22px 59px;
  display: flex;
  align-items: center;
  border: 1px solid $gainsboro;
}
.python {
  width: 10.05%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 177px;
  @include inter-32-semi-bold;
}
.week-4-q1 {
  width: 14.86%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 227px;
  @include inter-32-semi-bold;
}
.num-2 {
  width: 3.71%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 238px;
  @include inter-32-semi-bold;
}
.unsolved {
  width: 13.22%;
  color: $black;
  align-self: stretch;
  text-align: center;
  @include inter-32-semi-bold;
}
.flex-wrapper-three {
  background-color: $white-smoke;
  margin-bottom: 23px;
  margin-left: 1px;
  border-radius: 5px;
  padding: 22px 72px 23px 33px;
  display: flex;
  align-items: center;
  border: 1px solid $gainsboro;
}
.soft-engg {
  width: 14.43%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 118px;
  @include inter-32-semi-bold;
}
.quiz-1-syllabus {
  width: 21.1%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 194px;
  @include inter-32-semi-bold;
}
.num-1 {
  width: 3.34%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 260px;
  @include inter-32-semi-bold;
}
.solved {
  width: 9.56%;
  color: $black;
  align-self: stretch;
  text-align: center;
  @include inter-32-semi-bold;
}
.flex-wrapper-four {
  background-color: $white-smoke;
  margin-bottom: 272px;
  margin-left: 1px;
  border-radius: 5px;
  padding: 22px 72px 23px 58px;
  display: flex;
  align-items: center;
  border: 1px solid $gainsboro;
}
.python-two {
  width: 10.24%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 122px;
  @include inter-32-semi-bold;
}
.factorial-program {
  width: 25.28%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 172px;
  @include inter-32-semi-bold;
}
.num-2-two {
  width: 3.78%;
  color: $black;
  align-self: stretch;
  text-align: center;
  margin-right: 258px;
  @include inter-32-semi-bold;
}
.solved-two {
  width: 9.78%;
  color: $black;
  align-self: stretch;
  text-align: center;
  @include inter-32-semi-bold;
}
.vector-three {
  width: 4.11%;
  height: 5.61%;
  margin-left: 1148px;
}
</style>
