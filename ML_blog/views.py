from django.shortcuts import render 
from .models import Post

posts = [ # dummiey data
	{
		"author":"Rishi Joshi",
		"title":"Blog 1",
		"content":"First post content",
		"date_posted":"August 28,2018"
	},
	{
		"author":"Raksh Joshi",
		"title":"Blog 2",
		"content":"Second post content",
		"date_posted":"August 29,2018,"
	}
]
# now we can access this "posts" variable in template with the help of context variable      

def home(request):
	context = {
		'posts':Post.objects.all() # we can use key posts in template for using posts variable value
	}
	return render(request, 'ML_blog/home.html', context) # render(request,template path,context-pass_info_into_the_template)

def about(request):
	return render(request,'ML_blog/about.html',{'title':'about'}) # passing title
