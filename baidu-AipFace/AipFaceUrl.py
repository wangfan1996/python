from aip import AipFace
# 人脸检测
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

image = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1558171036676&di=f666ee7d2eae180f5bd239be01e69b08&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201505%2F18%2F20150518202417_23iCR.jpeg"

imageType = "URL"

""" 如果有可选参数 """
options = {}
options["face_field"] = "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype"
options["max_face_num"] = 1
options["face_type"] = "LIVE"

""" 带参数调用人脸检测 """
res = client.detect(image, imageType, options)
print(res)
# http://www.bejson.com/
# json格式校验
"""
{
	'error_code': 0,
	'error_msg': 'SUCCESS',
	'log_id': 304569281610491381,
	'timestamp': 1558161049,
	'cached': 0,
	'result': {
		'face_num': 1,
		'face_list': [{
			'face_token': '857750aaa141582bad422403c6974380',
			'location': {
				'left': 497.63,
				'top': 248.62,
				'width': 328,
				'height': 302,
				'rotation': 6
			},
			'face_probability': 1,
			'angle': {
				'yaw': -19.46,
				'pitch': 17.76,
				'roll': 11.57
			},
			'age': 23,
			'beauty': 77.36,
			'expression': {
				'type': 'none',
				'probability': 0.99
			},
			'face_shape': {
				'type': 'heart',
				'probability': 0.64
			},
			'gender': {
				'type': 'female',
				'probability': 1
			},
			'glasses': {
				'type': 'none',
				'probability': 1
			},
			'landmark': [{
				'x': 622.89,
				'y': 321.1
			}, {
				'x': 759.93,
				'y': 337.5
			}, {
				'x': 704.3,
				'y': 426.19
			}, {
				'x': 672.67,
				'y': 491.51
			}],
			'landmark72': [{
				'x': 493.8,
				'y': 277.24
			}, {
				'x': 492.88,
				'y': 335.07
			}, {
				'x': 496.46,
				'y': 393.83
			}, {
				'x': 508.84,
				'y': 453.89
			}, {
				'x': 549.29,
				'y': 513.94
			}, {
				'x': 602.87,
				'y': 557.28
			}, {
				'x': 658.76,
				'y': 571.95
			}, {
				'x': 708.21,
				'y': 545.8
			}, {
				'x': 747.4,
				'y': 501.74
			}, {
				'x': 774.76,
				'y': 459.26
			}, {
				'x': 796.52,
				'y': 416.03
			}, {
				'x': 810.52,
				'y': 371.27
			}, {
				'x': 819.14,
				'y': 326.1
			}, {
				'x': 588.88,
				'y': 318.34
			}, {
				'x': 609.67,
				'y': 309.68
			}, {
				'x': 629.74,
				'y': 309.49
			}, {
				'x': 646.79,
				'y': 317.97
			}, {
				'x': 658.18,
				'y': 337.2
			}, {
				'x': 641.71,
				'y': 338.72
			}, {
				'x': 622.29,
				'y': 338.3
			}, {
				'x': 603.13,
				'y': 329.86
			}, {
				'x': 622.89,
				'y': 321.1
			}, {
				'x': 568.49,
				'y': 275.41
			}, {
				'x': 602.75,
				'y': 260.81
			}, {
				'x': 634.11,
				'y': 265.95
			}, {
				'x': 660.94,
				'y': 277.13
			}, {
				'x': 682.08,
				'y': 298.56
			}, {
				'x': 655.74,
				'y': 291.96
			}, {
				'x': 629.04,
				'y': 282.63
			}, {
				'x': 600.55,
				'y': 276
			}, {
				'x': 733.86,
				'y': 346.64
			}, {
				'x': 750.28,
				'y': 329.37
			}, {
				'x': 768.8,
				'y': 325.41
			}, {
				'x': 784.97,
				'y': 329.45
			}, {
				'x': 795.54,
				'y': 342.73
			}, {
				'x': 784.76,
				'y': 351.63
			}, {
				'x': 768.37,
				'y': 354.77
			}, {
				'x': 749.9,
				'y': 351.2
			}, {
				'x': 759.93,
				'y': 337.5
			}, {
				'x': 741.5,
				'y': 308.19
			}, {
				'x': 762.75,
				'y': 291.53
			}, {
				'x': 784.71,
				'y': 286.42
			}, {
				'x': 806.9,
				'y': 286.27
			}, {
				'x': 821.83,
				'y': 303.87
			}, {
				'x': 805.65,
				'y': 300.91
			}, {
				'x': 785.24,
				'y': 302.46
			}, {
				'x': 763.7,
				'y': 305.88
			}, {
				'x': 681.97,
				'y': 342.5
			}, {
				'x': 673.15,
				'y': 371.53
			}, {
				'x': 664.12,
				'y': 400.94
			}, {
				'x': 647.73,
				'y': 429.97
			}, {
				'x': 672.56,
				'y': 436.62
			}, {
				'x': 711.57,
				'y': 443.09
			}, {
				'x': 724.36,
				'y': 440.1
			}, {
				'x': 722.8,
				'y': 409.85
			}, {
				'x': 721.61,
				'y': 378.41
			}, {
				'x': 720.58,
				'y': 347.07
			}, {
				'x': 704.3,
				'y': 426.19
			}, {
				'x': 613.18,
				'y': 478.62
			}, {
				'x': 649.67,
				'y': 474.06
			}, {
				'x': 681.08,
				'y': 477.29
			}, {
				'x': 703.66,
				'y': 479.4
			}, {
				'x': 716.05,
				'y': 490.38
			}, {
				'x': 698.97,
				'y': 510.9
			}, {
				'x': 671.84,
				'y': 517.81
			}, {
				'x': 638.06,
				'y': 505.47
			}, {
				'x': 648.97,
				'y': 484.57
			}, {
				'x': 678.34,
				'y': 489.91
			}, {
				'x': 700.45,
				'y': 490.33
			}, {
				'x': 696.55,
				'y': 495.48
			}, {
				'x': 674.63,
				'y': 496.06
			}, {
				'x': 646.01,
				'y': 490.92
			}],
			'race': {
				'type': 'yellow',
				'probability': 1
			},
			'quality': {
				'occlusion': {
					'left_eye': 0,
					'right_eye': 0,
					'nose': 0,
					'mouth': 0,
					'left_cheek': 0.02,
					'right_cheek': 0.02,
					'chin_contour': 0
				},
				'blur': 0,
				'illumination': 141,
				'completeness': 1
			},
			'face_type': {
				'type': 'human',
				'probability': 0.99
			}
		}]
	}
}
"""
