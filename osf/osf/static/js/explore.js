$(document).ready(function(){
	var isLogin = $('meta[name=isLogin]').attr('content');
	$('.explore .tags .tagbox a').live('click', function(){
		if(isLogin == 'false'){
			$('.ui.small.modal').modal('show');
			return false;
		}

		var tag_id = $(this).attr('id');
		var that = $(this);
		var url=basePath+'/tag/'+tag_id;
		var action=$(this).attr('action');

		$.ajax({
			url: basePath + '/tag/'+tag_id+'/'+action,
			type: 'GET',
			dataType: 'json'
		})
		.success(function(data){
			if(data.status == SUCCESS_INTEREST){
				$(that).text('已关注');
				$(that).attr('action', 'undointerest');
				$(that).parent('.hidden').removeClass();
				$(that).parent().addClass('interested');
				//css('opacity', '0.7');
			} else if(data.status=SUCCESS_INTEREST_UNDO){
				$(that).text('加关注');
				$(that).attr('action', 'interest');
				$(that).parent('.interested').removeClass()
				$(that).parent().addClass('hidden');
			}

		})

	});
})