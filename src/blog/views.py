from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import PostModel
from .forms import PostModelForm
def post_model_create_view(request):
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit = False)
		obj.save()

	context = {
		"form": form
	}
	template = "blog/create-view.html"
	return render(request, template, context)

def post_model_detail_view(request, id=None):
	# print(id)
	# obj = PostModel.objects.get(id=1)
	# try:
	# 	obj = PostModel.objects.get(id=100)
	# except:
	# 	raise Http404

	qs = PostModel.objects.filter(id=id)
	if not qs.exists():
		raise Http404
	else:
		obj = qs.first

	# obj = get_object_or_404(PostModel, id=1)
	template = "blog/detail-view.html"
	context = {
		"object": obj,
	}
	return render(request, template, context)

def post_model_list_view(request):
	print(request.user)
	qs = PostModel.objects.all()
	print(qs)
	template = "blog/list-view.html"
	context = {
		"object_list": qs,
	}
	return render(request, template, context)

@login_required(login_url = '/login')
def login_required_view(request):
	print(request.user)
	qs = PostModel.objects.all()
	context = {
		"object_list": qs,
	}
	if request.user.is_authenticated():
		template = "blog/list-view.html"
	else:
		template = "blog/list-view-public.html"
	return render(request, template, context)
