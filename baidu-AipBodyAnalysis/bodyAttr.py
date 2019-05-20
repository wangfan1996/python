from aip import AipBodyAnalysis

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example1.jpeg')

""" 调用人体检测与属性识别 """
client.bodyAttr(image);

""" 如果有可选参数 """
options = {}
options["type"] = "gender"

""" 带参数调用人体检测与属性识别 """
# res = client.bodyAttr(image, options)
res = client.bodyAttr(image)
print(res)
"""
{
	'person_num': 1,
	'person_info': [{人体姿态信息
		'attributes': {人体属性内容
			'upper_wear_fg': {上身服饰细分类
				'score': 0.3083132207393646,对应概率分数
				'name': 'T恤'T恤、无袖、衬衫、西装、毛衣、夹克、羽绒服、风衣、外套
			},
			'cellphone': {是否使用手机
				'score': 0.9998757839202881,对应概率分数
				'name': '未使用手机'未使用手机、使用手机、不确定
			},
			'lower_cut': {下方截断
				'score': 0.9986483454704285,对应概率分数
				'name': '无下方截断'无下方截断，有下方截断
			},
			'umbrella': {是否撑伞
				'score': 0.9997760653495789,对应概率分数
				'name': '未打伞'未撑伞、撑伞
			},
			'orientation': {身体朝向
				'score': 0.9993489384651184,对应概率分数
				'name': '正面'正面、背面、侧面
			},
			'is_human': {是否是正常人体
				'score': 0.9999946355819702,对应概率分数
				'name': '正常人体'正常人体，非正常人体
			},
			'headwear': {是否戴帽子
				'score': 0.7999138236045837,对应概率分数
				'name': '无帽'无帽、普通帽、安全帽
			},
			'gender': {性别
				'score': 0.7263807654380798,对应概率分数
				'name': '女性'男性、女性
			},
			'age': {年龄阶段
				'score': 0.7666301131248474,对应概率分数
				'name': '青年'幼儿、青少年、青年、中年、老年
			},
			'upper_cut': {上方截断
				'score': 0.9999711513519287,对应概率分数
				'name': '无上方截断'无上方截断，有上方截断
			},
			'glasses': {是否戴眼镜
				'score': 0.7515386939048767,对应概率分数
				'name': '无眼镜'戴眼镜、戴墨镜、无眼镜、不确定
			},
			'lower_color': {
				'score': 0.9966263771057129,对应概率分数
				'name': '白'
			},
			'bag': {
				'score': 0.9084603786468506,对应概率分数
				'name': '无背包'
			},
			'upper_wear_texture': {
				'score': 0.5662368535995483,对应概率分数
				'name': '纯色'
			},
			'smoke': {
				'score': 0.999985933303833,对应概率分数
				'name': '未吸烟'
			},
			'vehicle': {
				'score': 0.9999706745147705,对应概率分数
				'name': '无交通工具'
			},
			'lower_wear': {
				'score': 0.8789008855819702,对应概率分数
				'name': '长裙'
			},
			'carrying_item': {
				'score': 0.8695610761642456,对应概率分数
				'name': '无手提物'
			},
			'upper_wear': {
				'score': 0.7655608654022217,
				'name': '短袖'
			},
			'occlusion': {
				'score': 0.9982408285140991,
				'name': '无遮挡'
			},
			'upper_color': {
				'score': 0.932263970375061,
				'name': '蓝'
			}
		},
		'location': {
			'height': 1146,
			'width': 558,
			'top': 13,
			'score': 0.9994285702705383,
			'left': 87
		}
	}],
	'log_id': 2742402007015965844
}
"""
"""
{
	'person_num': 1,
	'person_info': [{
		'attributes': {
			'gender': {
				'score': 0.7263807654380798,
				'name': '女性'
			}
		},
		'location': {
			'height': 1146,
			'width': 558,
			'top': 13,
			'score': 0.9994285702705383,
			'left': 87
		}
	}],
	'log_id': 5632700670020167380
}
"""

"""
{
	'person_num': 6,
	'person_info': [{
		'attributes': {
			'gender': {
				'score': 0.8166012167930603,
				'name': '女性'
			}
		},
		'location': {
			'height': 290,
			'width': 140,
			'top': 125,
			'score': 0.982090413570404,
			'left': 169
		}
	}, {
		'attributes': {
			'gender': {
				'score': 0.8744381666183472,
				'name': '女性'
			}
		},
		'location': {
			'height': 262,
			'width': 109,
			'top': 126,
			'score': 0.9661603569984436,
			'left': 449
		}
	}, {
		'attributes': {
			'gender': {
				'score': 0.8794876933097839,
				'name': '女性'
			}
		},
		'location': {
			'height': 246,
			'width': 165,
			'top': 149,
			'score': 0.9346495866775513,
			'left': 280
		}
	}, {
		'attributes': {
			'gender': {
				'score': 0.8093627691268921,
				'name': '女性'
			}
		},
		'location': {
			'height': 324,
			'width': 98,
			'top': 70,
			'score': 0.7880557179450989,
			'left': 102
		}
	}, {
		'attributes': {
			'gender': {
				'score': 0.7835050225257874,
				'name': '女性'
			}
		},
		'location': {
			'height': 368,
			'width': 104,
			'top': 25,
			'score': 0.6790791749954224,
			'left': 533
		}
	}, {
		'attributes': {
			'gender': {
				'score': 0.866295576095581,
				'name': '女性'
			}
		},
		'location': {
			'height': 276,
			'width': 81,
			'top': 67,
			'score': 0.6451934576034546,
			'left': 266
		}
	}],
	'log_id': 6453736886607371956
}
"""
