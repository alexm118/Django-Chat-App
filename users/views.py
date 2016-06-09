from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

from users.models import ChatUser
from users.forms import ChatUserForm



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