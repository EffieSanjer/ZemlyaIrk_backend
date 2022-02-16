Highcharts.chart('container', {
	chart: {
		type: 'line'
	},
	title: {
		text: 'График изменения цены в этом районе'
	},
	subtitle: {
		text: 'с 1января 2011 по 31 декабря 2011'
	},
	xAxis: {
		categories: ['Янвврь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
	},
	yAxis: {
		title: {
			text: 'Цена в тыс. руб/сотку'
		}
	},
	plotOptions: {
		line: {
			dataLabels: {
				enabled: true
			},
			enableMouseTracking: false
		}
	},
	series: [{
		name: 'Цена',
		data: [700, 690, 950, 877, 765, 678, 689, 800, 831, 900, 899, 878]
	}, {
		name: 'Цена 2',
		data: [743, 656, 555, 678, 765, 678, 634, 844, 724, 900, 899, 878]
	},
	{
		name: 'Цена 3',
		data: [743, 656]}
	]
});