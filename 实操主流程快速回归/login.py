from 实操主流程快速回归 import encrypt
import requests
import json
import config


# APP登录接口,获取token
def login(username,password):
    url = test_config + "/basic/login"
    headers = {'content-type': 'application/json'}
    # 密码加密
    password = myEncrypt(password)

    data = {"userName":username,"password":password}
    re = requests.post(url,json=data,headers=headers)
    token = json.loads(re.text)["data"]["access_token"]  # 响应体先转字典，然后取token

    return token




# data = login("234210027","test123456")
# print(data)