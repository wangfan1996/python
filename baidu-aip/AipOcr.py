from aip import AipOcr
# 通用文字识别
""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpeg')

""" 调用通用文字识别, 图片参数为本地图片 """
res = client.basicGeneral(image);
print("唯一的log id", res['log_id'])
print("识别结果数，表示words_result的元素个数", res['words_result_num'])
for x in res['words_result']:
    print(x['words'])

"""
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

url = "http//www.x.com/sample.jpg"
""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
""" 带参数调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url, options)
"""
