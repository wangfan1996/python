from aip import AipOcr
# 身份证识别
""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('sfzz.jpg')
#front - 身份证含照片的一面 back - 身份证带国徽的一面
idCardSide = "front"

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["detect_risk"] = "true"

""" 带参数调用身份证识别 """
res = client.idcard(image, idCardSide, options)
print(res)



image1 = get_file_content('sfzf.png')
#front - 身份证含照片的一面 back - 身份证带国徽的一面
idCardSide1 = "back"

""" 如果有可选参数 """
options1 = {}
options1["detect_direction"] = "true"
options1["detect_risk"] = "true"

""" 带参数调用身份证识别 """
res1 = client.idcard(image1, idCardSide1, options1)
print(res1)

