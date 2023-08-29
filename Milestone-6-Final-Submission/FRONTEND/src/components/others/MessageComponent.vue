<template>
  <div>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: ''
    };
  },
  mounted() {
    axios.get('http://localhost:5000/api/message')
      .then(response => {
        this.message = response.data.message;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>
