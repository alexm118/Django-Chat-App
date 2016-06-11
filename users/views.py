from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from users.models import UserProfile
from users.forms import UserForm, UserProfileForm



def register(request):

	if request.method == 'GET':
		form = UserForm()
		greeting = 'Please register an account'

		context = {
			'form': form,
			'greeting': greeting
		}
		
		return render(request, 'users/register.html', context)

	else:
		form = UserForm(request.POST)
		
		if form.is_valid():
			user = User(username=form.cleaned_data['username'],
				email=form.cleaned_data['email'], 
				first_name=form.cleaned_data['first_name'], 
				last_name=form.cleaned_data['last_name'])
			user.set_password(form.cleaned_data['password'])
			user.save()
			profile = UserProfile(user=user)
			profile.save()
			return redirect('/login/')
		else:
			context = {
				'form': form,
				'greeting': 'Invalid fields, please check errors.'
			}
			return render(request, 'users/register.html', context)

def user_login(request):

	if request.method == 'GET':
		form = AuthenticationForm()
		greeting = 'Please Login'

		context = {
			'form': form,
			'greeting': greeting
		}

		return render(request, 'users/login.html', context)

	else:
		form = AuthenticationForm(data=request.POST)
		if request.user.is_authenticated():
			print('logging out old user?')
			logout(request)

		if form.is_valid():
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/profile/')
				else:
					print('User is disabled')
					return redirect('/login/')
			else:
				print('Invalid Login')
				context = {
					'form': form,
					'greeting': 'Invalid fields, please check errors.'
				} 
				return render(request, 'users/login.html', context)
		else:
			print(form.errors)
			context = {
				'form': form,
				'greeting': 'Invalid fields, please check errors.'
			}
			return render(request, 'users/login.html', context) 

def update_profile(request):
	if request.user.is_authenticated():
		print('User is logged in.')
		if request.method == 'GET':
			form = UserProfileForm()
			user = request.user
			context = {
				'form': form,
				'user': user
			}
			return render(request, 'users/update_profile.html', context)
	else:
		print('No user is logged in.')

def profile(request):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		profile = UserProfile.objects.get(user=user)
		context = {
			'user': user,
			'profile': profile
		}
		return render(request, 'users/profile.html', context)
	else:
		return redirect('/login/')