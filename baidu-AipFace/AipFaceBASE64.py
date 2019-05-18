from aip import AipFace
import base64


# 人脸检测
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath ="a.jpeg"
with open(filePath,"rb") as f:  
# b64encode是编码
    base64_data = base64.b64encode(f.read())

image = str(base64_data,'utf-8')
imageType = "BASE64"
""" 如果有可选参数 """
options = {}
options["face_field"] = "age,beauty,expression,faceshape,gender,glasses,race,quality,facetype"
options["max_face_num"] = 1
options["face_type"] = "LIVE"

""" 带参数调用人脸检测 """
res = client.detect(image, imageType, options)
print(res)
"""{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 305486881619989161,
	'timestamp': 1558161998,
	'cached': 0,
	'result': {
		'face_num': 1,//检测到的图片中的人脸数量
		'face_list': [{//人脸信息列表，具体包含的参数参考下面的列表。
			'face_token': '857750aaa141582bad422403c6974380',//人脸图片的唯一标识
			'location': {//人脸在图片中的位置
				'left': 497.63,//人脸区域离左边界的距离
				'top': 248.62,//人脸区域离上边界的距离
				'width': 328,//人脸区域的宽度
				'height': 302,//人脸区域的高度
				'rotation': 6//人脸框相对于竖直方向的顺时针旋转角，[-180,180]
			},
			'face_probability': 1,//人脸置信度，范围【0~1】，代表这是一张人脸的概率，0最小、1最大。
			'angle': {//人脸旋转角度参数
				'yaw': -19.46,//三维旋转之左右旋转角[-90(左), 90(右)]
				'pitch': 17.76,//三维旋转之俯仰角度[-90(上), 90(下)]
				'roll': 11.57//平面内旋转角[-180(逆时针), 180(顺时针)]
			},
			'age': 23,//年龄 ，当face_field包含age时返回
			'beauty': 77.36,//美丑打分，范围0-100，越大表示越美。当face_fields包含beauty时返回
			'expression': {//表情，当 face_field包含expression时返回
				'type': 'none',//none:不笑；smile:微笑；laugh:大笑
				'probability': 0.99//表情置信度，范围【0~1】，0最小、1最大。
			},
			'face_shape': {//脸型，当face_field包含faceshape时返回
				'type': 'heart',//square: 正方形 triangle:三角形 oval: 椭圆 heart: 心形 round: 圆形
				'probability': 0.64//置信度，范围【0~1】，代表这是人脸形状判断正确的概率，0最小、1最大。
			},
			'gender': {//性别，face_field包含gender时返回
				'type': 'female',//male:男性 female:女性
				'probability': 1//性别置信度，范围【0~1】，0代表概率最小、1代表最大。
			},
			'glasses': {//是否带眼镜，face_field包含glasses时返回
				'type': 'none',//none:无眼镜，common:普通眼镜，sun:墨镜
				'probability': 1//眼镜置信度，范围【0~1】，0代表概率最小、1代表最大。
			},
			'race': {//人种 face_field包含race时返回
				'type': 'yellow',//yellow: 黄种人 white: 白种人 black:黑种人 arabs: 阿拉伯人
				'probability': 1//人种置信度，范围【0~1】，0代表概率最小、1代表最大。
			},
			'quality': {//人脸质量信息。face_field包含quality时返回
				'occlusion': {//人脸各部分遮挡的概率，范围[0~1]，0表示完整，1表示不完整
					'left_eye': 0,//左眼遮挡比例
					'right_eye': 0,//右眼遮挡比例
					'nose': 0,//鼻子遮挡比例
					'mouth': 0,//嘴巴遮挡比例
					'left_cheek': 0.02,//	左脸颊遮挡比例
					'right_cheek': 0.02,//右脸颊遮挡比例
					'chin_contour': 0//下巴遮挡比例
				},
				'blur': 0,//人脸模糊程度，范围[0~1]，0表示清晰，1表示模糊
				'illumination': 141,//取值范围在[0~255], 表示脸部区域的光照程度 越大表示光照越好
				'completeness': 1//人脸完整度，0或1, 0为人脸溢出图像边界，1为人脸都在图像边界内
			},
			'face_type': {//真实人脸/卡通人脸 face_field包含face_type时返回
				'type': 'human',//human: 真实人脸 cartoon: 卡通人脸
				'probability': 0.99//人脸类型判断正确的置信度，范围【0~1】，0代表概率最小、1代表最大。
			}
		}]
	}
}"""
