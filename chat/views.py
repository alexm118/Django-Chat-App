from django.shortcuts import render, redirect

from .models import Room

from .forms import RoomForm, ChatForm

# Create your views here.

def chat_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'chat/chat_list.html', context)

def new_chat(request):
    if request.method == 'GET':
        form = RoomForm()
        context = {
            'form': form
        }
        return render(request, 'chat/new_chat.html', context)
    else:
        form = RoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            label = form.cleaned_data['label']
            room = Room(name=name, label=label)
            room.save()
            return redirect('/chat/{0}/'.format(label))
        else:
            return render(request, 'chat/new_chat.html', {'form': form})
def chat_room(request, label):
    room = Room.objects.get(label=label)
    form = ChatForm()
    context = {
        'room': room,
        'form': form
    }
    return render(request, 'chat/chat_room.html', context)