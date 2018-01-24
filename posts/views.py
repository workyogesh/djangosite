from django.shortcuts import render
from .models import Post
from  django.utils import timezone
# Create your views here.
def  post_title(request):
	post = Post.objects.filter(published_date__lte=timezone.now()).order_by('create_date')
	return render(request,'posts/post_list.html',{'post':post})
