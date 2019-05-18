from aip import AipOcr

# 银行卡识别
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('yhk.jpeg')

""" 调用银行卡识别 """
res = client.bankcard(image);
print(res)
"""
{'log_id': 8878518492261451666, 'result': {'bank_card_number': '6217 0038 1002 6896 707', 'valid_date': '07/24', 'bank_card_type': 1, 'bank_name': '建设银行'}}
"""
