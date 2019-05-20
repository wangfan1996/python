import os
import sys
import time
from aip import AipBodyAnalysis

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

imageList = os.listdir('./gesture')

for x in imageList:
    imgUrl = 'gesture/' + x
    image = get_file_content(imgUrl)
    print(imgUrl)
    """ 调用手势识别 """
    res = client.gesture(image);
    print(res)
    time.sleep(2)
