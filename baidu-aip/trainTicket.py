from aip import AipOcr

# 火车票识别
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('hcp.png')

""" 调用银行卡识别 """
res = client.trainTicket(image);
print(res)
"""
{'log_id': 1619889705590922834, 'words_result_num': 8, 'words_result': {'name': '', 'destination_station': '重庆北', 'seat_category': '新空调硬卧', 'ticket_rates': '羊410.00元', 'ticket_num': '0007645', 'date': '2012年06月20日18:24开', 'train_num': 'K336次', 'starting_station': '厦门'}}
"""
