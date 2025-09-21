const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: [
      'Books Issued',
      'New Books Arrived',
      'Books Overdue',
      'Books Sold'
    ],
    datasets: [{
      label: 'Weekly Book Analytics',
      data: [35, 73, 27, 65],
      backgroundColor: [
        '#0AF4FB',
        '#F59D0B',
        '#D30BF5',
        '#0FB982'
      ],
      hoverOffset: 4
    }]
  },
  options: {
    cutout: '75%',
    rotation: 90
  }
})
