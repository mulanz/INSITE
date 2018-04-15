Chart.defaults.global.defaultFontColor = 'white';
Chart.defaults.global.defaultFontSize = 25;
Chart.defaults.global.defaultFontFamily = 'Abel';
var labels = ['extroversion', 'curiosity', 'self-will', 'dumbass']
var values = [30.9, 94.2, 93.9, 89.5];

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: labels,
    datasets: [
      {
        data: values,
        backgroundColor: [
                'white',
                'white',
                'white',
                'white'
            ],
        label: 'Most Valued Traits',
        fill: false
      }
    ]
  }
});
