from aip import AipFace
import base64
# 用户信息查询
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

groupId = "user_admin"
userId = "user1"

""" 调用用户信息查询 """
res = client.getUser(userId, groupId);
print(res)
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281648191261,
	'timestamp': 1558164819,
	'cached': 0,
	'result': {
		'user_list': [{
			'user_info': '',
			'group_id': 'user_admin'
		}]
	}
}
"""

""" 调用获取用户人脸列表 """
res = client.faceGetlist(userId, groupId);
print(res)
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 305486881649014192,
	'timestamp': 1558164901,
	'cached': 0,
	'result': {
		'face_list': [{
			'face_token': '857750aaa141582bad422403c6974380',
			'ctime': '2019-05-18 15:23:02'
		}, {
			'face_token': 'd55ea0d38d300820f8a9d4606902d45c',
			'ctime': '2019-05-18 15:26:43'
		}, {
			'face_token': '293db2174feee7a94b1fb46e414a0341',
			'ctime': '2019-05-18 15:27:09'
		}]
	}
}
"""
"""
https://console.bce.baidu.com/ai/s/facelib/face?appId=999945&groupId=user_admin&uid=user1&faceId=d55ea0d38d300820f8a9d4606902d45c
"""
