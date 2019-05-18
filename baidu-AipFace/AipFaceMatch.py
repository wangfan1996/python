from aip import AipFace
import base64
# 用户信息查询
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

groupId = "user_admin"
userId = "user1"

""" 调用获取用户人脸列表 """
res = client.faceGetlist(userId, groupId);
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
matchList = []
if(res['error_msg']=='SUCCESS'):
    for item in res['result']['face_list']:
        imageItem = {'image':item['face_token'],'image_type':'FACE_TOKEN',}
        matchList.append(imageItem)

result = client.match(matchList[0:2])
print(result)
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281660994201,
	'timestamp': 1558166099,
	'cached': 0,
	'result': {
		'score': 84.90947723,//是	float	人脸相似度得分
		'face_list': [{//是	array	人脸信息列表
			'face_token': '857750aaa141582bad422403c6974380'//是	string	人脸的唯一标志
		}, {
			'face_token': 'd55ea0d38d300820f8a9d4606902d45c'
		}]
	}
}
"""
