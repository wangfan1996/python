import itchat

#登陆
itchat.auto_login()
#获取自己的信息
my = itchat.search_friends()
#昵称
my['NickName']
#username
my['UserName']
#传备注的名称查出来人
user = itchat.search_friends(name='罗跃婷')
"""
[<User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@53d51cbb82f4d693d75fbf77cf60b7f865116a1f9aff22c93a5d460260f35e18', 'NickName': '(=^・ω・^=)', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=667851079&username=@53d51cbb82f4d693d75fbf77cf60b7f865116a1f9aff22c93a5d460260f35e18&skey=@crypt_c0f521be_00d40af6f2cd1946c53c715781284fd0', 'ContactFlag': 2051, 'MemberCount': 0, 'RemarkName': '罗跃婷', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '做一件让自己感动的事🤔', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': '??', 'PYQuanPin': '??', 'RemarkPYInitial': '??LYT', 'RemarkPYQuanPin': '??luoyueting', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4197, 'Province': '河北', 'City': '廊坊', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0, 'HeadImgUpdateFlag': 1, 'ContactType': 0, 'ChatRoomOwner': ''}>]
"""
#传入UserName查出来人
user = itchat.search_friends(userName='@53d51cbb82f4d693d75fbf77cf60b7f865116a1f9aff22c93a5d460260f35e18')
#发送消息
user.send("hello word")
#获取公众号
gzh = itchat.get_mps()
#查找公众号
gzh = itchat.search_mps(name="校锐星")
"""
[<MassivePlatform: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@64010ab7433f67442613d16e90466888', 'NickName': '校锐星', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=667939364&username=@64010ab7433f67442613d16e90466888&skey=@crypt_c0f521be_00d40af6f2cd1946c53c715781284fd0', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 0, 'Signature': '让学校运营管理更高效', 'VerifyFlag': 24, 'OwnerUin': 0, 'PYInitial': 'JRX', 'PYQuanPin': 'jiaoruixing', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 0, 'Province': '湖南', 'City': '长沙', 'Alias': '', 'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': 'gh_', 'EncryChatRoomId': '', 'IsOwner': 0}>]
"""
gzh = itchat.search_mps(userName='@64010ab7433f67442613d16e90466888')
"""
<MassivePlatform: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@64010ab7433f67442613d16e90466888', 'NickName': '校锐星', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=667939364&username=@64010ab7433f67442613d16e90466888&skey=@crypt_c0f521be_00d40af6f2cd1946c53c715781284fd0', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 0, 'Signature': '让学校运营管理更高效', 'VerifyFlag': 24, 'OwnerUin': 0, 'PYInitial': 'JRX', 'PYQuanPin': 'jiaoruixing', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 0, 'Province': '湖南', 'City': '长沙', 'Alias': '', 'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': 'gh_', 'EncryChatRoomId': '', 'IsOwner': 0}>
"""
#返回完整的群聊列表
gc = itchat.get_chatrooms()
#获取名字中含有特定字符的群聊
gc = itchat.search_chatrooms(name='帆')

#发送文件
user = itchat.search_friends(name='罗跃婷')
itchat.send_file('2.jpg',user[0]['UserName'])
"""
<ItchatReturnValue: {'BaseResponse': {'Ret': 0, 'ErrMsg': '请求成功', 'RawMsg': '请求成功'}, 'MsgID': '5968094431724074482', 'LocalID': '15572095502206'}>
"""
itchat.send_file('1.txt',user[0]['UserName'])
"""
<ItchatReturnValue: {'BaseResponse': {'Ret': 0, 'ErrMsg': '请求成功', 'RawMsg': '请求成功'}, 'MsgID': '6965294053539133624', 'LocalID': '15572095543841'}>

"""
#发送图片
itchat.send_image('2.jpg',user[0]['UserName'])
<ItchatReturnValue: {'BaseResponse': {'Ret': 0, 'ErrMsg': '请求成功', 'RawMsg': '请求成功'}, 'MsgID': '2102696151695048713', 'LocalID': '15572099777139'}>















