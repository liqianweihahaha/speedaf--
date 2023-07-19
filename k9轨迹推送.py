import requests
import json,time,sys
import DesUtils

appCode = "888888"
secretKey = "hvmaYYOyegNy4muv"


# 入库
def inStorage(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
	"time": "2021-01-10 14:23:01",
	"action": "150",
	"mailNo": mailNo,
	"msgEng": "[广州花都仓] [InternationalLogistics] [InternationalLogistics]  processing, order has been inbounded",
	"msgLoc": "[广州花都仓] [InternationalLogistics] [InternationalLogistics]  processing, order has been inbounded",
	"weight": 0.506,
	"country": "Nigeria",
	"message": "[广州花都仓] [InternationalLogistics] [InternationalLogistics] 进行处理，订单已操作入库",
	"optCode": "234102001",
	"optName": "InternationalLogistics",
	"timezone": 8,
	"actionName": "入库",
	"sourceCode": "K9",
	"countryCode": "NG"
    }
]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}

    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 集包
def Package(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-27 11:00:31",
    "action":"181",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"国际二部集包",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"国际二部集包",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(res)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)

# 出库
def OUT_STORAGE(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-27 12:00:31",
    "action":"190",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"国际二部出库",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"国际二部出库",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)

# 国内交接完成
def INLAND_CONNECT(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-27 13:00:31",
    "action":"191",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"国内交接完成",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"国内交接完成",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)

# 航班起飞
def FLIGHT(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-27 14:00:31",
    "action":"220",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"航班起飞",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"航班起飞",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)

# 航班落地
def LAND(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2022-11-27 15:00:31",
    "action":"230",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"航班落地",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"航班落地",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 报关
def CUSTOMS_CLEARANCE(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-27 16:00:31",
    "action":"401",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"报关",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"报关",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 清关中
def CUSTOMS(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 10:00:31",
    "action":"360",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"清关中",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"清关中",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 清关完成
def CUSTOMS_FINISH(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 11:00:31",
    "action":"370",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"清关完成",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"清关完成",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 清关异常
def ABNORMAL_CLEARANCE(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 12:00:31",
    "action":"401",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"清关异常",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"清关异常",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 派送到中心仓
def DISP_DC_PC(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 13:00:31",
    "action":"375",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"派送到中心仓",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"派送到中心仓",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 揽件
def PICKED(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 15:00:31",
    "action":"1",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"揽件",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"揽件",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 发件
def SHIPPING_FROM(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 16:00:31",
    "action":"2",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"发件",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"发件",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 到件
def SHIPPING_TO(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 17:00:31",
    "action":"3",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"到件",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"到件",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 派送中
def DELIVERING(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 18:00:31",
    "action":"4",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"派送中",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"派送中",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "goodsLength": "100",
    "goodsWidth": "100",
    "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    # online = 'https://apis.speedaf.com/'
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 已签收
def COLLECTED(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2021-11-28 19:00:31",
    "action":"5",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"已签收",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"已签收",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
        "goodsLength": "100",
        "goodsWidth": "100",
        "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    # online = 'https://apis.speedaf.com/'
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 退件签收
def RETURN_COLLECTED(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2022-02-15 19:00:31",
    "action":"730",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"退件签收",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"退件签收",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
        "goodsLength": "100",
        "goodsWidth": "100",
        "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    # online = 'https://apis.speedaf.com/'
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


# 退件中
def UN_DELIVER(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "time":"2022-02-14 19:00:31",
    "action":"-710",
    "mailNo":mailNo,
    "msgEng":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc":"【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "weight":1,
    "country":"Nigeria",
    "message":"退件中",
    "optCode":"86001",
    "optName":"jack",
    "timezone":8,
    "actionName":"退件中",
    "sourceCode":"K9",
    "countryCode":"NG",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
        "goodsLength": "100",
        "goodsWidth": "100",
        "goodsHeight": "100"
}]

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    # online = 'https://apis.speedaf.com/'
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    # print the response text (the content of the requested file):
    re = json.loads(res.text)
    print(re)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)


if __name__ == "__main__":

    # config = sys.argv[2]
    # mailNo = sys.argv[1]


    mailNo = "47233200794189"
    # uat_config = "http://112.74.53.147:8480"
    # uat_config = "https://apis.speedaf.com"
    # uat_config = "http://47.241.40.42:8480"
    # test_config = "http://172.19.29.189:8480"
    uat_config = "http://47.241.92.41:8480"
    # uat_config = "http://10.240.3.206:8480"



    # inStorage(mailNo,uat_config)  #入库
    # time.sleep(2)
    # Package(mailNo,uat_config) #集包
    # time.sleep(2)
    # OUT_STORAGE(mailNo,uat_config)#出库
    # time.sleep(2)
    # INLAND_CONNECT(mailNo,uat_config)#国内交接完成
    # time.sleep(2)
    # FLIGHT(mailNo,uat_config)  #航班起飞
    # time.sleep(2)
    # LAND(mailNo,uat_config)  # 航班降落
    # time.sleep(2)
    # CUSTOMS_CLEARANCE(mailNo,uat_config)  # 报关
    # time.sleep(2)
    # CUSTOMS(mailNo,uat_config)  # 清关中
    # time.sleep(2)
    # CUSTOMS_FINISH(mailNo,uat_config)  # 清关完成
    # time.sleep(2)
    # ABNORMAL_CLEARANCE(mailNo,uat_config)  # 清关异常
    # time.sleep(2)
    # #
    # DISP_DC_PC(mailNo,uat_config)  # 派送到中心仓
    # time.sleep(2)
    PICKED(mailNo,uat_config)  # 揽收
    # time.sleep(2)
    # SHIPPING_FROM(mailNo,uat_config) # 发件
    # time.sleep(2)
    # SHIPPING_TO(mailNo,uat_config)  # 到件
    # time.sleep(2)
    # DELIVERING(mailNo,uat_config)  # 派送中
    # time.sleep(2)
    # COLLECTED(mailNo,uat_config)  # 签收
    # time.sleep(2)



    # UN_DELIVER(mailNo,uat_config)  # 退件中

    # RETURN_COLLECTED(mailNo,uat_config) # 退件签收

