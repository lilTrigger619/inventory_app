
console.log("hhs");
const $inventoryLevelChart = document.querySelector("#inventory_level_ctx"); // line chart
const $inventoryTypeRate = document.querySelector("#inventory-type-rate"); // donut chart
const lineChart = $inventoryLevelChart.getContext("2d");
const donutChart = $inventoryTypeRate.getContext("2d");

const lineData = {
	labels: ["Jan", "Feb", "March", "April", "May", "June", "July"],
	datasets: [
		{
			label: "Inventory level",
			data: [65, 59, 80, 81, 56, 55, 40],
			fill: false,
			borderColor: "rgb(75, 192, 192)",
			tension: 0.1,
		},
	],
};

const donutData = {
  labels: [
    'Red',
    'Blue',
    'Yellow'
  ],
  datasets: [{
    label: 'My First Dataset',
    data: [300, 50, 100],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4,
	  cutout:"70%",
	  radius: "60%",
  }]

};

const line1 = new Chart(lineChart, {
	type: "line",
	data:lineData,
});

const donut1 = new Chart(donutChart, {
	type: "doughnut",
	data:donutData,
});
