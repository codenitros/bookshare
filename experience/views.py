from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post#,likes

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'experience/post_list.html', {'posts': posts})

def detail_view(request,id = None):
	post = get_object_or_404(Post, id=id)
	context = {'post':post,}
	return render(request,'experience/detail_view.html',context)

