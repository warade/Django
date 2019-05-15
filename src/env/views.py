from django.http import HttpResponse, HttpResponseRedirect

# def home(request):
# 	print(request.method)
# 	print(request.get_full_path())
# 	print(request.is_ajax)
# 	print(request.is_ajax())
# 	return HttpResponse('<h1> hello world </h1>')

def home(request):
	response = HttpResponse(content_type = 'text/html')
	response.content = '<h1> Hello New World <h1>'

	return response

def redirect_somewhere(request):
	return HttpResponseRedirect("/some/path")