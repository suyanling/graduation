$(document).ready(function() {
	/*
	实现scrollspy功能
	 */
	$('body').scrollspy({
		target: '#navbar_su'
	});
	$('[data-spy="scroll"]').each(function() {
		var $spy = $(this).scrollspy('refresh')
	})

	/*
	实现左边导航条第二级菜单的显示和隐藏
	 */
	$('.nav_taggle').mouseover(function() {
		$('.nav_taggle').find('ul').hide()
		$(this).find('ul').show()
			// console.log($(this))
	})
	$('.nav_taggle').mouseout(function() {
			$('.nav_taggle').find('ul').hide()
		})
		/*
		实现input下拉列表，下拉列表中的选项填入input中
		 */
		// $(selector).on(event,childSelector,data,function,map)
	$('.my_ullist').on('click', '.selet', function() {
			var tmp = $(this).text();
			var oInput = $(this).parents('.input-group').find('.userchoose');
			/*
			把字符串里的空格和空行删除,使用正则表达式,替换
			 */
			// console.log("1"+tmp)
			tmp = tmp.replace(/\s/g, "");
			// console.log("1"+tmp)
			oInput.val(tmp);
		})
		/*
		阻止下拉标题的点击事件
		 */
		// $('.dropdown-header').click(function(ev) {
		// 	ev.stopPropagation();
		// })
		/*
		
		 */
		// $('.submitS').click(function() {
		// 	$('.selectINFO').show();
		// })
})