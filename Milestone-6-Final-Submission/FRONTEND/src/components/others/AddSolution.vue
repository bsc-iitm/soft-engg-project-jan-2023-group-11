<template>
    <div class="component-4">
      <div class="rectangle-6"></div>
      <div class="rectangle-7"></div>
      <div class="minus"><div class="vector"></div></div>
      <p class="author-phil-dunphy">Author: Phil Dunphy</p>
      <p class="week-4-q1">Week 4 Q1</p>
      <p class="in-the-first-line-we-are-using-multiple">
        In the first line, we are using multiple assignments
        in one line. So, after the first line of execution,
        xa, y &#61; b and z &#61; c. In the second line, we
        Know that operator has the right to left
        associativity. So, the value of z which is c, will be
        assigned to y and the value of y which is now c, will
        be assigned to x. So finally, all variables will
        contain the same value c.<br />
        <br />
        Hence, (a) and (d) are correct.
      </p>
      <div class="rectangle-11"></div>
      <div class="group-14">
        <p class="post">POST</p>
        <img
          alt=""
          class="vector-two"
          src="https://static.overlay-tech.com/assets/bd0260c2-9744-40ba-bfac-c221ef69eda2.svg"
        />
      </div>
      <div class="window-restore">
        <img
          alt=""
          class="vector-three"
          src="https://static.overlay-tech.com/assets/1fbd7337-0748-4ab6-95d8-b3d3de201372.svg"
        />
      </div>
      <div class="window-close">
        <img
          alt=""
          class="vector-three"
          src="https://static.overlay-tech.com/assets/7da47302-daf3-46c9-bfdd-25c3b46860ca.svg"
        />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AddSolution"
  };
  </script>
  
  <style lang="scss" scoped>
  .component-4 {
    padding: 0 1px 0 0;
  }
  .rectangle-6 {
    width: 99.59%;
    height: 13.58%;
    background-color: $teal-2;
    border-radius: 10px 10px 0px 0px;
    position: absolute;
    left: 1px;
    top: 0;
    border: 2px solid $teal-2;
  }
  .rectangle-7 {
    width: 99.84%;
    height: 99.67%;
    background-color: $white-smoke;
    border-radius: 10px;
    position: relative;
    border: 1px solid $teal-2;
  }
  .minus {
    width: calc(1.97% - 10px);
    height: calc(3.97% - 22px);
    padding: 11px 5px;
    display: flex;
    align-items: center;
    position: absolute;
    right: 104px;
    top: 31px;
  }
  .vector {
    background-color: $white;
    flex: 1;
    align-self: stretch;
  }
  .author-phil-dunphy {
    width: 25.39%;
    height: 6.46%;
    color: $white-smoke;
    text-align: center;
    position: absolute;
    right: 453px;
    top: 24px;
    @include inter-32-semi-bold;
  }
  .week-4-q1 {
    width: 13.48%;
    height: 6.46%;
    color: $white-smoke;
    text-align: center;
    position: absolute;
    left: 38px;
    top: 24px;
    @include inter-32-semi-bold;
  }
  .in-the-first-line-we-are-using-multiple {
    height: 47.68%;
    width: 92.93%;
    font-family: "Inter";
    font-size: 32px;
    font-weight: 500;
    line-height: normal;
    color: $black;
    display: flex;
    position: absolute;
    right: 42px;
    top: 139px;
  }
  .rectangle-11 {
    width: 17.5%;
    height: 11.26%;
    background-color: $teal-2;
    border-radius: 10px;
    position: absolute;
    right: 25px;
    bottom: 30px;
  }
  .group-14 {
    display: flex;
    align-items: center;
    position: absolute;
    right: 56px;
    bottom: 46px;
  }
  .post {
    width: 63.85%;
    font-family: "Inter";
    font-size: 30px;
    font-weight: 700;
    line-height: normal;
    color: $white-smoke;
    align-self: stretch;
    text-align: center;
    margin-right: 23px;
  }
  .vector-two {
    width: 18.46%;
    height: 58.33%;
  }
  .window-restore {
    width: calc(1.97% - 8px);
    height: calc(3.97% - 8px);
    padding: 4px;
    display: flex;
    align-items: center;
    position: absolute;
    right: 68px;
    top: 31px;
  }
  .vector-three {
    flex: 1;
    align-self: stretch;
    object-fit: cover;
  }
  .window-close {
    width: calc(1.97% - 10px);
    height: calc(3.97% - 10px);
    padding: 5px;
    display: flex;
    align-items: center;
    position: absolute;
    right: 29px;
    top: 31px;
  }
  </style>