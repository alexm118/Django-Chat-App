from django.forms import ModelForm
from django import forms
from users.models import ChatUser
from django.contrib.auth.models import User

class ChatUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
	
    class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())