google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(domainPieChart);

var temp = {{domains_count|safe}};
//mapping occurences of each unique type of domain:
counts = {};
for (var i = 0; i < temp.length; i++) {
	counts[temp[i]] = 1 + (counts[temp[i]] || 0);
}

var count = Object.keys(counts).map(key => counts[key]);
var domains = Object.keys(counts).map(key => key);

var rows = [];
for (var i=0; i<count.length;i++) {
	rows.push([ domains[i], count[i] ]);
}

function domainPieChart(){
	var data = new google.visualization.DataTable();
	data.addColumn('string','Domain');
	data.addColumn('number','Ocurrences');
	data.addRows(rows);

	var options = {
		chartArea: { width: '100%', height: '100%'},
		fontName: 'Rajdhani',
		title: 'Territory of projects',
		pieHole: 0.30,
		backgroundColor: 'transparent',
		legend: {
  textStyle: {
    fontSize: 14
  }
}
	};
	var chart = new google.visualization.PieChart(document.getElementById('domain-chart'));
	chart.draw(data, options);
}

