from channels import Group
from channels.sessions import channel_session

@channel_session
def ws_message(message):
    Group('chat-{0}'.format(message.channel_session['room'])).send({
        'text': message['text'],
    })

@channel_session
def ws_connect(message):
    room = message.content['path'].strip('/')
    message.channel_session['room'] = room
    Group('chat-{0}'.format(room)).add(message.reply_channel)

@channel_session
def ws_disconnect(message):
    Group('chat-{0}'.format(message.channel_session['room'])).discard(message.reply_channel)
