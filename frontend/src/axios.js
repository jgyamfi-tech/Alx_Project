import axios from 'axios';

// Create an Axios instance
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',  // URL of your Django backend API
  headers: {
    'Content-Type': 'application/json',
  },
});

// Intercept requests to add Authorization token if it's present in localStorage
instance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default instance;
