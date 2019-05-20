from aip import AipImageSearch

APP_ID = '16291996'
API_KEY = 'YpSjGKiK2xWAKqtn9kLmGQ0x'
SECRET_KEY = 'g6wqdpMK5thRyZPacwr8TEodZdRj8mHC'

client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpeg')

""" 调用相同图检索—检索, 图片参数为本地图片 """
client.sameHqSearch(image);
""" 如果有可选参数 """
options = {}
options["tags"] = "100,11"#1 - 65535范围内的整数，tag间以逗号分隔，最多2个tag。样例："100,11" ；检索时可圈定分类维度进行检索
options["tag_logic"] = "0"#检索时tag之间的逻辑， 0：逻辑and，1：逻辑or
options["pn"] = "0"#分页功能，起始位置，例：0。未指定分页时，默认返回前300个结果；接口返回数量最大限制1000条，例如：起始位置为900，截取条数500条，接口也只返回第900 - 1000条的结果，共计100条
options["rn"] = "1"#分页功能，截取条数，例：250

""" 带参数调用相同图检索—检索, 图片参数为本地图片 """
res = client.sameHqSearch(image, options)
print(res)
"""
{
    'has_more': False,是否还有下一页，返回值：true、false；如果不分页，不用关注该字段
    'log_id': 2195535274485387028,唯一的log id，用于问题定位
    'result_num': 1,检索结果数
    'result': [
        {
            'score': 0.99747755253923,图片相关性，0-1
            'brief': '{调用add接口添加的brief信息，为保证该结果有效性，请入库是填写有效可关联至本地图片库的有效id信息
                "name": "周杰伦",
                "id": "666"
            }',
            'cont_sign': '3966446724,
            3332070207'图片签名，可以用来删除图片或定位问题
        }
    ]
}
"""
