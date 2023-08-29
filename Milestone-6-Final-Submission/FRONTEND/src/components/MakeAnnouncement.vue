<template>
    <div class="component-5">
      <div class="flex-wrapper-two">
        <p class="python">Python</p>
        <img
          alt=""
          class="vector"
          src="https://static.overlay-tech.com/assets/66f58866-f1d7-4347-8baf-5592d5f48531.svg"
        />
      </div>
      <p class="the-python-quiz-is-scheduled-for-26th-fe">
        The Python quiz is scheduled for 26th February 2023
        from 2- 6 pm. Syllabus: Week 1 - 4
      </p>
      <div class="flex-wrapper-one">
        <div class="group-14">
          <p class="post">POST</p>
          <img
            alt=""
            class="vector-two"
            src="https://static.overlay-tech.com/assets/833f5657-9d9d-4cfb-919a-af3e5d60368c.svg"
          />
        </div>
      </div>
      <div class="flex-wrapper-three">
        <p class="make-an-announcement">
          Make an announcement
        </p>
        <img
          alt=""
          class="vector-three"
          src="https://static.overlay-tech.com/assets/d9bfb6cb-5d62-4424-a677-1c803bd361f0.svg"
        />
        <div class="minus">
          <div class="vector-four"></div>
        </div>
        <div class="window-restore">
          <img
            alt=""
            class="vector-five"
            src="https://static.overlay-tech.com/assets/93c533fa-cf82-4ca2-bf1b-fea59860f749.svg"
          />
        </div>
        <div class="window-close">
          <img
            alt=""
            class="vector-five"
            src="https://static.overlay-tech.com/assets/2d03629e-30b0-4c4a-ada3-f0b0ff34ba8d.svg"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "MakeAnnouncement"
  };
  </script>
  
  <style lang="scss" scoped>
  .component-5 {
    position: absolute;
    // width: 60%;
    background-color: whitesmoke;
    border-radius: 10px;
    right: 5px;
    bottom: 5px;
    margin: 50px 400px 20px 20px;
    padding: 130px 22px 24px 70px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    border: 1px solid #026277;
  }
  .flex-wrapper-two {
    background-color: white;
    margin-bottom: 69px;
    border-radius: 10px;
    padding: 16px 17px 16px 29px;
    display: flex;
    align-items: center;
    border: 1px solid gainsboro;
  }
  .python {
    width: 26.18%;
    color: #026277;
    align-self: stretch;
    text-align: center;
    margin-right: 289px;
  }
  .vector {
    width: 5.66%;
    height: 38.46%;
  }
  .the-python-quiz-is-scheduled-for-26th-fe {
    height: 19.41%;
    width: 94.72%;
    font-family: "Inter";
    font-size: 18px;
    font-weight: 500;
    line-height: normal;
    color: black;
    display: flex;
    margin-bottom: 118px;
  }
  .flex-wrapper-one {
    background-color: #026277;
    margin-left: 696px;
    border-radius: 10px;
    padding: 16px 31px 16px 32px;
    display: flex;
    align-items: center;
  }
  .group-14 {
    display: flex;
    align-items: center;
  }
  .post {
    width: 55.33%;
    font-family: "Inter";
    font-size: 18px;
    font-weight: 700;
    line-height: normal;
    color: whitesmoke;
    align-self: stretch;
    text-align: center;
    margin-right: 40px;
  }
  .vector-two {
    width: 16%;
    height: 58.33%;
  }
  .flex-wrapper-three {
    background-color: #026277;
    width: 93.5%;
    border-radius: 10px 10px 0px 0px;
    padding: 24px 29px 19px 33px;
    display: flex;
    align-items:center;
    justify-content: space-between;
    position: absolute;
    left: -1px;
    top: -1px;
    border: 2px solid #026277;
  }
  .make-an-announcement {
    width: 39.59%;
    color: whitesmoke;
    align-self: stretch;
    text-align: center;
    font-size: 24px;
    font-weight: 500;
    margin-right: 20px;
  }
  .vector-three {
    width: 2.56%;
    height: 61.54%;
    margin-top: 8px;
    margin-right: 423px;
  }
  .minus {
    width: calc(2.64% - 10px);
    margin-top: 8px;
    height: 2px;
    margin-right: 32px;
    padding: 11px 5px;
    display: flex;
    align-items: center;
    align-self: stretch;
  }
  .vector-four {
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
  .vector-five {
    flex: 1;
    align-self: stretch;
    object-fit: cover;
  }
  .window-close {
    width: calc(2.56% - 10px);
    height: calc(61.54% - 10px);
    margin-top: 5px;
    padding: 5px;
    display: flex;
    align-items: center;
  }
  </style>