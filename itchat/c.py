import itchat
from itchat.content import *

@itchat.msg_register(TEXT)

def text_reply(msg):
    for key,value in msg.items():
       print(key,value)

@itchat.msg_register(PICTURE)

def picture_reply(msg):
    for key,value in msg.items():
       print(key,value)

itchat.auto_login()
itchat.run()

