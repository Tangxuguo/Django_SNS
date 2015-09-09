basePath = '';
img_base_url= 'http://7xjfbe.com1.z0.glb.clouddn.com/';
post_cover_thumbnail='?imageView2/2/w/500';
album_thumbnail='?imageView2/1/w/200/h/200';

		var current_version = 'develop';
var osf = {
		develop:{
			basePath:'',
			post_cover_style:null,
			album_thumbnail:null
		},
		release:{
			basePath:'',
			post_cover_style:'@!postcover',
			album_thumbnail:'@!albumthumbnail'
		}
		
}
function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}

$(document).ready(function() {
	var photos = [];
	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
		beforeSend: function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	})