
import requests,json

def pickScan(waybillCode):
    url = "http://112.74.181.248:3000/basic/manager/pickedScan/add"
    headers = {'Content-Type': 'application/json',
               'Authorization': "880220039:ec022902-f557-424f-9a33-119693f35847",
               'lang': "zh_CN",
               'Connection': 'close'}

    data = {"weight": "1", "waybillCode": waybillCode}

    re = requests.post(url, json=data, headers=headers)
    re = json.loads(re.text)  # 字符串转成字典
    if re["success"] == True:
        print("揽件扫描成功")
    else:
        print("揽件扫描失败", re)



def signScan(waybillCode):
    url = "http://112.74.181.248:3000/basic/manager/sign/deliver/add"
    headers = {'Content-Type': 'application/json',
               'Authorization': "880220039:ec022902-f557-424f-9a33-119693f35847",
               'lang': "zh_CN",
               'Connection': 'close'}

    data = {
            "waybillCode":waybillCode,
            "photoUrl":"517f5f2b-59a7-4343-9226-ff5fb7253941.png",
        }

    re = requests.post(url,json=data,headers=headers)
    re = json.loads(re.text)  # 字符串转成字典
    if re["success"] == True:
        print("正常签收成功")
    else:
        print("正常签收失败",re)


def exceptionSignScan(waybillCode):
    url = "http://112.74.181.248:3000/basic/manager/sign/exception/add"
    headers = {'Content-Type': 'application/json',
               'Authorization': "880220039:ec022902-f557-424f-9a33-119693f35847",
               'lang': "zh_CN",
               'Connection': 'close'}

    data = {
            "exceptionType": 731,   # 731代表的是电话不通或错误     730代表退件签收
            "signer":"tata",
            "waybillCode": waybillCode,
            "remark":"autotest",
            "photoUrl":"517f5f2b-59a7-4343-9226-ff5fb7253941.png"
        }

    re = requests.post(url,json=data,headers=headers)
    re = json.loads(re.text)  # 字符串转成字典
    if re["success"] == True:
        print("异常签收扫描成功")
    else:
        print("异常签收扫描失败",re)


i = 0
while i < 4:
    # pickScan("BD021011509437")
    # signScan('BD021011509437')
    exceptionSignScan('BD021011509437')
    i = i + 1
print('Good bye!')
