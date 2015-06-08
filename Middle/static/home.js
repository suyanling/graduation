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
		// console.log(target);
		var namesArray = new Array();
		var tmp = '';
		var oInput = '';
		select.on('click', '.selet', function() {
			tmp = $(this).text();
			oInput = $(this).parents('.input-group').find('.userchoose');

			// 把字符串里的空格和空行删除,使用正则表达式,替换

			// console.log("1"+tmp)
			tmp = tmp.replace(/\s/g, "");

			oInput.val(tmp);
			// 当选择多产品时
			if (target == '#selectNames') {
				targetDom = $(target);
				// target.text(tmp);
				var carnames = $('#selectNames span').text();
				// console.log(carnames);
				carnames = carnames.split(" ");
				// carnames.pop();
				// 判断用户是否已经选择该产品？是：添加；不是：不添加
				var key = $.inArray(tmp, carnames);
				if (carnames.length > 5) {
					alert("最多只能选择5个");
					return;
				}
				if (key < 0) {
					carnames.push(tmp);
					// 给span里面的内容加一个空格，为了后面获取（分离）每一个span的内容
					var innername = '<span class="label label-default ">' + tmp + " " + '</span>' + '	';
					targetDom.append(innername);
				}
			}
		});
		// 选择多属性时
		if (target == '#selectProperties') {
			targetDomP = $(target);
			// console.log($(select[0]).parents('.input-group').find('.userchoose').val())
			// console.log($(select[1]).parents('.input-group').find('.userchoose').val())
			// console.log(propertyArray);
			$("#sureSelect").click(function() {
				var propertyArray = [];
				// 对多属性和其相应的权值进行处理，把属性拿出来，
				// 作为接下来的判重
				var carproperty = $('#selectProperties span').text();
				carproperty = carproperty.split(" ");

				// 出去最后的一个空字符
				carproperty.pop();
				
				// 把属性拿出来
				for (var prop in carproperty) {
					var tmparray = carproperty[prop].split('*');
					propertyArray.push(tmparray[0]);
				}

				selectP1Dom = $(select[0]).parents('.input-group').find('.userchoose');
				selectP2Dom = $(select[1]).parents('.input-group').find('.userchoose');
				selectP1 = selectP1Dom.val();
				selectP2 = selectP2Dom.val();

				// 最多选择5个属性
				if (propertyArray.length > 4) {
					alert("最多选择5个属性");
				}
				// 判断用户是否已经选择该属性？是：添加；不是：不添加
				var key = $.inArray(selectP1, propertyArray);
				if (selectP1 != "" && selectP2 != "" && key < 0) {
					propertyArray.push(selectP1);
					var tmpstr = selectP1 + "*" + selectP2;
					var innername = '<span class="label label-default ">' + tmpstr + " " + '</span>' + '	';
					targetDomP.append(innername);
				} else if (selectP1 == "") {
					alert("请同时选择名字！");
				} else if (selectP2 == "") {
					alert("请同时选择权值！");
				}

				console.log(propertyArray);
			});
		}
	};
	// 选择单产品的下拉列表
	downlist($('.my_ullist'), "");

	// 选择多产品的下拉列表
	downlist($('.my_ullist_m'), '#selectNames');
	downlist($('.my_ullist_p'), '#selectProperties');
	/*
	阻止下拉标题的点击事件
	 */
	// $('.dropdown-header').click(function(ev) {
	// 	ev.stopPropagation();
	// })
	/*
		
	 */
	$(".selectitem").on("click","span",function(event){
		// var carnames = $('#selectNames span').text();
		// 在DOM结构中删除元素，在原来的数组
		$(this).remove();
	});

});