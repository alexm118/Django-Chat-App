from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.chat_list, name='chatlist'),
    url(r'new/$', views.new_chat, name='createroom'),
    url(r'^(?P<label>[\w]+)/', views.chat_room, name="chatroom")
]
