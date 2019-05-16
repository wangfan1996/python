import itchat

#登陆
itchat.auto_login(hotReload=True)
#获取自己的信息
f = itchat.get_friends()

print(f)
exit()
print(f[-1])
for key,value in f[-1].items():
    print(key,value)

"""
MemberList []
Uin 0
UserName @da89fdbbaf909a7b6a9e90ce4a66fa0a
NickName 我的名字
HeadImgUrl /cgi-bin/mmwebwx-bin/webwxgeticon?seq=667943384&username=@da89fdbbaf909a7b6a9e90ce4a66fa0a&skey=@crypt_c0f521be_aa67d0a9711ebe5aea6af180196b54be
ContactFlag 3
MemberCount 0
RemarkName 阮鹏卿
HideInputBarFlag 0
Sex 1
Signature 心上无垢，林间有风
VerifyFlag 0
OwnerUin 0
PYInitial WDMZ
PYQuanPin wodemingzi
RemarkPYInitial RPQ
RemarkPYQuanPin ruanpengqing
StarFriend 0
AppAccountFlag 0
Statues 0
AttrStatus 233919
Province 北京
City 东城
Alias 
SnsFlag 17
UniFriend 0
DisplayName 
ChatRoomId 0
KeyWord rua
EncryChatRoomId 
IsOwner 0
"""
