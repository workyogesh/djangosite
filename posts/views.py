from django.shortcuts import render, get_object_or_404
from .models import Post,Contact
from django.http import Http404
from  django.utils import timezone
from .forms import Contact_form
# Create your views here.
def  post_title(request):
	post = Post.objects.filter(published_date__lte=timezone.now()).order_by('create_date')
	return render(request,'posts/post_list.html',{'post':post})

def post_detail(request,pk):
	
	try:
		detail = get_object_or_404(Post,pk=pk)
		
	except Exception as e:
		raise Http404("Page not found77")
	return render(request,'posts/post_detail.html',{'detail':detail})
		

def contact(request):
	return render(request,'posts/contact.html',{})

def forum_list(request):
	forum=Post.objects.all()
	return render(request,'posts/forum_list.html',{'forum':forum})

def contact_submit(request):
	if request.method=='POST':
		form=Contact_form(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'posts/contact.html',{'id':1})

		else:
			return render(request,'posts/contact.html',{'id':0})
	