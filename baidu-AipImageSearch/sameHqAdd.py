from aip import AipImageSearch

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpeg')

""" 如果有可选参数 """
options = {}
options["brief"] = "{\"name\":\"周杰伦\", \"id\":\"666\"}"#检索时原样带回,最长256B。
options["tags"] = "100,10"#1 - 65535范围内的整数，tag间以逗号分隔，最多2个tag。样例："100,11" ；检索时可圈定分类维度进行检索

""" 带参数调用相同图检索—入库, 图片参数为本地图片 """
res = client.sameHqAdd(image, options)
print(res)
"""
{
  'log_id': 2262825443116807284,唯一的log id，用于问题定位
  'cont_sign': '20175919,384875704'输入图片签名，可用于删除
}
已存在
{'log_id': 7673034800508489684, 'error_code': 216681, 'cont_sign': '20175919,384875704', 'error_msg': 'item has existed'}
"""

#url = "http//www.x.com/sample.jpg"
""" 如果有可选参数 """
#options = {}
#options["brief"] = "{\"name\":\"周杰伦\", \"id\":\"666\"}"
#options["tags"] = "100,11"
""" 带参数调用相同图检索—入库, 图片参数为远程url图片 """
#client.sameHqAddUrl(url, options)

