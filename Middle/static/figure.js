$(document).ready(function() {
	var name = $('#selectName').text();
	var property = $('#selectProperty').text();
	/* 
	本来想让输入框中保存选择的名称和属性，提升用户的体验，但是，
	这样，就不能单独选择汽车名称了
	var property = $('#selectProperty').text();
	console.log(property);
	$('.chooseproperty').val(property);
	$('.choosename').val(name);*/

	// console.log(name);
	// 请求表单的数据
	// 汽车名之前是表单提交的时候获取，再传入相应的实现函数，实现起来比较麻烦
	// 使用下面的方法，直接把汽车名传过去，这样比较简单
	/**********使用饼图来展示，改变成使用折线来展示。因为饼图对于负数和为0的数，不展示*********/
	// $.getJSON('/singlefigure/?carname=' + name, function(ret) {
	// 	console.log(ret);
	// 	console.log(ret['内饰']);
	// 	var data = [
	// 		['内饰', ret['内饰']],
	// 		['动力', ret['动力']],
	// 		['售后', ret['售后']],
	// 		['外观', ret['外观']],
	// 		['安全性', ret['安全性']],
	// 		['性价比', ret['性价比']],
	// 		['操控', ret['操控']],
	// 		['油耗', ret['油耗']],
	// 		['空间', ret['空间']],
	// 		['舒适性', ret['舒适性']]
	// 	];
	// 	var plot1 = jQuery.jqplot('SinglePie', [data], {
	// 		seriesDefaults: {
	// 			// Make this a pie chart.
	// 			renderer: jQuery.jqplot.PieRenderer,
	// 			rendererOptions: {
	// 				// Put data labels on the pie slices.
	// 				// By default, labels show the percentage of the slice.
	// 				showDataLabels: true
	// 			}
	// 		},
	// 		legend: {
	// 			show: true,
	// 			location: 'e'
	// 		}
	// 	});
	// });
	/*var data = [{
		'内饰':'1',
		'动力':'1',
		'售后':'1',
		'外观':'1',
		'安全性':'1',
		'性价比':'1',
		'操控':'1',
		'油耗':'1',
		'空间':'1',
		'舒适性':'1'
	}];
	var plot2 = $.jqplot('SinglePie', [data], {
		// Give the plot a title.
		title: 'Plot With Options',
		// You can specify options for all axes on the plot at once with
		// the axesDefaults object.  Here, we're using a canvas renderer
		// to draw the axis label which allows rotated text.
		axesDefaults: {
			labelRenderer: $.jqplot.CanvasAxisLabelRenderer
		},
		// An axes object holds options for all axes.
		// Allowable axes are xaxis, x2axis, yaxis, y2axis, y3axis, ...
		// Up to 9 y axes are supported.
		axes: {
			// options for each axis are specified in seperate option objects.
			xaxis: {
				label: "X Axis",
				// Turn off "padding".  This will allow data point to lie on the
				// edges of the grid.  Default padding is 1.2 and will keep all
				// points inside the bounds of the grid.
				pad: 0
			},
			yaxis: {
				label: "Y Axis"
			}
		}
	});*/

	/**********************由折线改为使用bar（柱状图来展示）***************************/
	/*
	根据用户的选择生成相应的图像。
	用户选择汽车名和属性名
	用户只是选择汽车名 则请求'/singlefigure/?carname=' + name
	用户只是选择属性名，则请求'/singlefigure1/?carname=' + property
	 */
	if (name != "" && property != "") {
		$.getJSON('/singlefigure2/?carname=' + name + '&carproperty=' + property, function(ret) {
			pirture("Chart3", ret);
		});
		$('.graphicAll').show();
		$('.graphicFeature').hide();
		$('.graphicName').hide();
	}
	if (name != "" && property == "") {
		$('.graphicName').show();
		$('.graphicFeature').hide();
		$('.graphicAll').hide();
		$.getJSON('/singlefigure/?carname=' + name, function(ret) {
			pirture("Chart1", ret);
		});

	}
	if (property != "" && name == "") {
		$('.graphicName').hide();
		$('.graphicAll').hide();
		$('.graphicFeature').show();

		$.getJSON('/singlefigure1/?carproperty=' + property, function(ret) {
			if (ret == "") {
				$('.graphicFeature').hide();
			}
			// innername是推荐的汽车的名字
			var innername = '';
			/*
			先检验返回的数据是什么样的格式，再根据相应的数据结果处理
			 */
			console.log(ret[0][0]);
			console.log(ret);
			var arrayfigure = [];
			for (var i = 0; i < ret.length; i++) {
				innername += '<span class="label label-default">' + ret[i][0] + '</span>' + '	';
				var tmparray = [];
				tmparray.push(ret[i][0]);
				tmparray.push(parseInt(ret[i][1]));
				console.log(tmparray);
				arrayfigure.push(tmparray);
			}
			$('.recomProperty').append(innername);
			/*
			图像展示汽车对应的属性好坏
			 */
			var plot1 = jQuery.jqplot('Chart2', [arrayfigure], {
				seriesDefaults: {
					// Make this a pie chart.
					renderer: jQuery.jqplot.PieRenderer,
					rendererOptions: {
						// Put data labels on the pie slices.
						// By default, labels show the percentage of the slice.
						showDataLabels: true
					}
				},
				legend: {
					show: true,
					location: 'e'
				}
			});

		});
	}

	function pirture(chart, ret) {
		/****************************/
		/*
		本来是想把属性值为0的数值变成0.05
		这样在图表上就可以展示，而且所展比值不大
		 */
		// var datafigure = [];
		// for (var key in ret) {
		// 	if (ret[key] == 0) {
		// 		ret[key] == "0.05";
		// 		console.log(0.05)
		// 	}
		// 	datafigure.push(ret[key])
		// }
		// console.log(datafigure);
		/****************************/
		// var s1 = [ret['内饰']];
		// var s2 = [ret['动力']];
		// var s3 = [ret['售后']];
		// var s4 = [ret['外观']];
		// var s5 = [ret['安全性']];
		// var s6 = [ret['性价比']];
		// var s7 = [ret['操控']];
		// var s8 = [ret['油耗']];
		// var s9 = [ret['空间']];
		// var s10 = [ret['舒适性']];
		// Can specify a custom tick Array.
		// Ticks should match up one for each y value (category) in the series.
		var ticks = [];
		var figuredata = [];
		var i = 1;
		var innername = '';
		for (var key in ret) {
			console.log(key);
			ticks.push(key);
			// 其他推荐的汽车名
			if (key != name) {
				innername += '<span class="label label-default">' + key + '</span>' + '	';
			}
			/* 
			这样得到的figuredata是包含是个数组的数组
			0: Array[10]
			1: Array[10]
			2: Array[10]
			3: Array[10]
			而jqplot要传进去的数据的格式却是要包含十个数组的数组
			var tmparray = []
			for(var value in ret[key]) {
				tmparray.push(ret[key][value]);
			}
			console.log(tmparray);
			figuredata.push(tmparray)*/
		}
		$('.recomNames').append(innername);
		/*
		利用$.each('要处理的json数据', function(i, item){}) i
		i 是key值， item 是对应的value值
		 */
		$.each(ret, function(i, item) {
			// console.log(i);
			// console.log(item);
			var tmparray = []
				// console.log(ret[i]);
			$.each(item, function(j, item) {
				// console.log(j);
				// console.log(item);
				tmparray.push(item);
			});
			figuredata.push(tmparray);
		});
		console.log(figuredata)
			/*
			把数组figuredata的行和列翻转
			 */
		var arrayfigure = []
		for (var i = 0; i < 10; i++) {
			var tmp = [];
			arrayfigure.push(tmp)
		}
		for (var i = 0; i < figuredata.length; i++) {
			for (var j = 0; j < figuredata[i].length; j++) {
				arrayfigure[j].push(figuredata[i][j]);
			}
			// console.log(s1);
		}
		console.log(arrayfigure);
		/*
		为什么直接使用datafigure数组这样的格式不可以不可以
		一定要使用[s1, s2, s3,s4,s5,s6,s7,s8,s9,s10]
		这样的格式
		 */
		// var plot1 = $.jqplot('Chart1',datafigure, {
		var plot1 = $.jqplot(chart, arrayfigure, {
			// The "seriesDefaults" option is an options object that will
			// be applied to all series in the chart.
			seriesDefaults: {
				renderer: $.jqplot.BarRenderer,
				rendererOptions: {
					fillToZero: true
				}
			},
			// Custom labels for the series are specified with the "label"
			// option on the series option.  Here a series option object
			// is specified for each series.
			series: [{
				label: '空间'
			}, {
				label: '动力'
			}, {
				label: '操控'
			}, {
				label: '油耗'
			}, {
				label: '舒适性'
			}, {
				label: '外观'
			}, {
				label: '内饰'
			}, {
				label: '性价比'
			}, {
				label: '售后'
			}, {
				label: '安全性'
			}],
			// Show the legend and put it outside the grid, but inside the
			// plot container, shrinking the grid to accomodate the legend.
			// A value of "outside" would not shrink the grid and allow
			// the legend to overflow the container.
			legend: {
				show: true,
				placement: 'outsideGrid'
			},
			axes: {
				// Use a category axis on the x axis and use our custom ticks.
				xaxis: {
					renderer: $.jqplot.CategoryAxisRenderer,
					ticks: ticks
				},
				// Pad the y axis just a little so bars can get close to, but
				// not touch, the grid boundaries.  1.2 is the default padding.
				yaxis: {
					// pad: 1,
					// tickOptions: {
					// 	formatString: '$%d'
					// }
				}
			},
			grid: {
				drawGridLines: true,
				background: "#FFF"
			}
		});
	}


});