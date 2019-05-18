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

#用户上传过来的图片
filePath ="d.jpeg"
with open(filePath,"rb") as f:  
# b64encode是编码
    base64_data = base64.b64encode(f.read())
image = str(base64_data,'utf-8')
imageType = "BASE64"

matchResult = []
if(res['error_msg']=='SUCCESS'):
    for item in res['result']['face_list']:
        matchArr = [{'image':image,'image_type':imageType,}]
        imageItem = {'image':item['face_token'],'image_type':'FACE_TOKEN'}
        matchArr.insert(1,imageItem)
        result = client.match(matchArr)
        matchResult.insert(1,result)

print(matchResult)
"""
[{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281670877601,
	'timestamp': 1558167087,
	'cached': 0,
	'result': {
		'score': 94.33959961,
		'face_list': [{
			'face_token': '53a81b0d16a8f2562e67f392b77b73fb'
		}, {
			'face_token': '857750aaa141582bad422403c6974380'
		}]
	}
}, {
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281670884371,
	'timestamp': 1558167088,
	'cached': 0,
	'result': {
		'score': 91.7686615,
		'face_list': [{
			'face_token': '53a81b0d16a8f2562e67f392b77b73fb'
		}, {
			'face_token': '293db2174feee7a94b1fb46e414a0341'
		}]
	}
}, {
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281670881051,
	'timestamp': 1558167088,
	'cached': 0,
	'result': {
		'score': 93.0076828,
		'face_list': [{
			'face_token': '53a81b0d16a8f2562e67f392b77b73fb'
		}, {
			'face_token': 'd55ea0d38d300820f8a9d4606902d45c'
		}]
	}
}]
"""

