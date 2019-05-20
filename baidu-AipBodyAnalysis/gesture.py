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

image = get_file_content('gesture/One.png')

""" 调用手势识别 """
res = client.gesture(image);

print(res)
"""
{
    'log_id': 4063029987777103252,唯一的log id，用于问题定位
    'result_num': 1,结果数量
    'result': [检测到的目标，手势、人脸
        {
            'probability': 0.7583031058311462,目标属于该类别的概率
            'top': 17,目标框上坐标
            'height': 66,目标框的高
            'classname': 'One',	目标所属类别，24种手势、other、face
            'width': 44,目标框的宽
            'left': 45目标框最左坐标
        }
    ]
}
"""
