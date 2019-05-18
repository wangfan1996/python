import requests
import json

API_KEY = ''
SECRET_KEY = ''

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
headers = {'Content-Type':'application/json; charset=UTF-8'}
AccessToken = requests.post(host,headers=headers)
print(AccessToken)
AccessTokenJson = AccessToken.json()
print(AccessTokenJson)
"""
{'refresh_token': '25.ba858d289dd5c9a942fff926ea65e28b.315360000.1873508418.282335-16273941', 'expires_in': 2592000, 'session_key': '9mzdXUDw14G2TpAL8/lLtB5ZM4AZu1X58Bae8s+2jcKOpA1YjDoOgfA6RPa8UqLc+Krm+Cr6KT+NyYgFOhJ3pK499c0jZQ==', 'access_token': '24.f4498e3eef50fb1ad5afaf66fe94e6e3.2592000.1560740418.282335-16273941', 'scope': 'public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr brain_ocr_handwriting brain_ocr_passport brain_ocr_vat_invoice brain_numbers brain_ocr_train_ticket brain_ocr_taxi_receipt vis-ocr_车辆vin码识别 vis-ocr_定额发票识别 brain_ocr_vin brain_ocr_quota_invoice wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi', 'session_secret': '5465e551af491a6e6a89972913196b71'}
"""
Access_Token = '24.f4498e3eef50fb1ad5afaf66fe94e6e3.2592000.1560740418.282335-16273941'
