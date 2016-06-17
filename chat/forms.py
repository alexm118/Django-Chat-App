from django.forms import ModelForm

from .models import Room, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'label')

class ChatForm(ModelForm):
    class Meta:
        model = Message
        fields = ('message',)
