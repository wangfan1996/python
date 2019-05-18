from aip import AipFace
import base64
# 人脸注册
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath ="c.jpeg"
with open(filePath,"rb") as f:  
# b64encode是编码
    base64_data = base64.b64encode(f.read())

image = str(base64_data,'utf-8')
imageType = "BASE64"
groupId = "user_admin"
userId = "user1"

""" 如果有可选参数 """
options = {}
options["user_info"] = "user's info"
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"
""" 带参数调用人脸检测 """
res = client.addUser(image, imageType, groupId, userId);
print(res)
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 305486881641816031,
	'timestamp': 1558164181,
	'cached': 0,
	'result': {
		'face_token': '857750aaa141582bad422403c6974380',
		'location': {
			'left': 497.63,
			'top': 248.62,
			'width': 328,
			'height': 302,
			'rotation': 6
		}
	}
}
"""
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281644028521,
	'timestamp': 1558164402,
	'cached': 0,
	'result': {
		'face_token': 'd55ea0d38d300820f8a9d4606902d45c',
		'location': {
			'left': 476.9,
			'top': 550.26,
			'width': 381,
			'height': 394,
			'rotation': -5
		}
	}
}
"""
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 305486881644293191,
	'timestamp': 1558164429,
	'cached': 0,
	'result': {
		'face_token': '293db2174feee7a94b1fb46e414a0341',
		'location': {
			'left': 969.21,
			'top': 1006.38,
			'width': 787,
			'height': 721,
			'rotation': -21
		}
	}
}
"""
