<template>
    <div>
      <canvas id="performanceChart" width="400" height="200"></canvas>
    </div>
  </template>
  
  <script>
  // Import Chart.js
  import { Chart } from 'chart.js';
  
  export default {
    data() {
      return {
        // Sample data for the chart
        chartData: {
          labels: ['Test 1', 'Test 2', 'Test 3', 'Test 4'],
          datasets: [
            {
              label: 'Student Performance',
              data: [85, 90, 92, 88],  // Replace with actual data
              borderColor: 'rgba(75, 192, 192, 1)',
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderWidth: 1,
            },
          ],
        },
      };
    },
    mounted() {
      this.renderChart();
    },
    methods: {
      renderChart() {
        // Create the chart when the component is mounted
        const ctx = document.getElementById('performanceChart').getContext('2d');
        new Chart(ctx, {
          type: 'line',  // You can change the chart type (e.g., bar, radar, etc.)
          data: this.chartData,
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Optionally add custom styling for the chart */
  #performanceChart {
    max-width: 100%;
  }
  </style>
  

