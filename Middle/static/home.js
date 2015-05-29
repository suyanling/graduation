$(document).ready(function() {
	/*
	实现scrollspy功能
	 */
	$('body').scrollspy({
		target: '#navbar_su'
	});
	$('[data-spy="scroll"]').each(function() {
		var $spy = $(this).scrollspy('refresh')
	});
	/*
	实现左边导航条第二级菜单的显示和隐藏
	 */
	$('.nav_taggle').mouseover(function() {
		$('.nav_taggle').find('ul').hide()
		$(this).find('ul').show()
			// console.log($(this))
	});
	$('.nav_taggle').mouseout(function() {
		$('.nav_taggle').find('ul').hide()
	});
	/*
	实现input下拉列表，下拉列表中的选项填入input中
	 */
	// $(selector).on(event,childSelector,data,function,map)


	$('#single_submit').click(function() {
		var name = $('.choosename').val();
		var property = $('.chooseproperty').val();
		if (name == "" && property == "") {
			alert("您提交了一个空表单");
			return false;
		}
	});
	/*
	function downlist(select, action){}是对页面中下拉菜单的操作
	select 是选择的下拉菜单
	target是选择该菜单时对其产生影响的DOM元素
	 */
	// }

	function downlist(select, target) {
		var namesArray = new Array();
		select.on('click', '.selet', function() {
			var tmp = $(this).text();
			var oInput = $(this).parents('.input-group').find('.userchoose');

			// 把字符串里的空格和空行删除,使用正则表达式,替换

			// console.log("1"+tmp)
			tmp = tmp.replace(/\s/g, "");
			// console.log("1"+tmp)
			oInput.val(tmp);

			// 当选择多产品时
			if (target != "") {
				// target.text(tmp);
				var carnames = $('#selectNames span').text();
				console.log(carnames);
				carnames = carnames.split(" ");
				// carnames.pop();
				// 判断用户是否已经选择该产品？是：添加；不是：不添加
				var key = $.inArray(tmp, carnames);
				if (carnames.length > 5) {
					alert("最多只能选择5个产品");
					return;
				}
				if (key < 0) {
					carnames.push(tmp);
					// 给span里面的内容加一个空格，为了后面获取（分离）每一个span的内容
					var innername = '<span class="label label-default ">' + tmp + " " + '</span>' + '	';
					target.append(innername);
				}
			}
		});
	};
	// 选择单产品的下拉列表
	downlist($('.my_ullist'), "");

	// 选择多产品的下拉列表
	downlist($('.my_ullist_m'), $('#selectNames'));
	/*
	阻止下拉标题的点击事件
	 */
	// $('.dropdown-header').click(function(ev) {
	// 	ev.stopPropagation();
	// })
	/*
		
	 */
	$("#selectNames").on("click","span",function(event){
		var carnames = $('#selectNames span').text();
		console.log($(this).text());
		// 在DOM结构中删除元素，在原来的数组
		$(this).remove();
		// carnames = carnames.split(" ");
		// console.log(carnames);
		// carnames.pop();
	});

});