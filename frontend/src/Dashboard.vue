<template>
    <div>
      <h1>Student Performance</h1>
      <PerformanceChart />
    </div>
  </template>
  
  <script>
  import PerformanceChart from './PerformanceChart.vue';  // Import the Chart Component
  
  export default {
    components: {
      PerformanceChart,  // Register the component
    },
  };
  </script>
  