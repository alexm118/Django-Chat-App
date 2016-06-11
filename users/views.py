from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from users.models import ChatUser
from users.forms import ChatUserForm, LoginForm



def register(request):

	if request.method == 'GET':
		form = ChatUserForm()
		greeting = 'Please register an account'

		context = {
			'form': form,
			'greeting': greeting
		}
		
		return render(request, 'users/register.html', context)

	else:
		form = ChatUserForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('/hello/')
		else:
			context = {
				'form': form,
				'greeting': 'Invalid fields, please check errors.'
			}
			return render(request, 'users/register.html', context)

def user_login(request):

	if request.method == 'GET':
		form = LoginForm
		greeting = 'Please Login'

		context = {
			'form': form,
			'greeting': greeting
		}

		return render(request, 'users/login.html', context)

	else:
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/hello/')
				else:
					print('User is disabled')
					return redirect('/hello/')
			else:
				print('Invalid Login')
				context = {
					'form': form,
					'greeting': 'Invalid fields, please check errors.'
				} 
				return render(request, 'users/login.html', context)
		else:
			context = {
				'form': form,
				'greeting': 'Invalid fields, please check errors.'
			}
			return render(request, 'users/login.html', context) 