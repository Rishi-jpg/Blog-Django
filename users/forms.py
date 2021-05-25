from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() # default required = True

	class Meta:
		model  = User # if we do model.save() it sould save in User model in admin
		fields = ['username','email','password1','password2'] # fields we want in form and what order, password 1 is creating pass and Password 2 is validating password
