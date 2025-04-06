<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" type="text" placeholder="Username" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from '../axios';  // Import the Axios instance
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('/auth/login/', {
            username: this.username,
            password: this.password,
          });
  
          // Store the token received from the API in localStorage
          localStorage.setItem('token', response.data.token);
          
          // Redirect to dashboard after successful login
          this.$router.push('/dashboard');
        } catch (error) {
          console.error("Error logging in:", error);
          // Optionally, show an error message to the user (e.g., a notification or alert)
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styling here (optional) */
  </style>
  