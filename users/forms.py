from django.forms import ModelForm
from users.models import ChatUser
from django.contrib.auth.models import User

class ChatUserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')