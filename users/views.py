from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

#types of messages
#1) messages.debug
#2) messages.info
#3) messages.success
#4) messages.warning
#5) messages.error

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() #saving form in database
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! You are now able to login')
			return redirect('login')
	else:	
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
	return render(request,'users/profile.html')
