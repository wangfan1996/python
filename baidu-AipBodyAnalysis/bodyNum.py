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

image = get_file_content('num.jpeg')

""" 调用人流量统计 """
res = client.bodyNum(image)
print(res)
"""
{'person_num': 16, 'log_id': 8015463418790948916}
"""
