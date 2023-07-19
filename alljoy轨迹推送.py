

import requests
import json,time,sys,random
import DesUtils

appCode = "888888"
secretKey = "hvmaYYOyegNy4muv"

import time
def get_now_time():
    """
    获取当前日期时间
    :return:当前日期时间
    """
    now =  time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)  # 获取当前时间

    # 转为时间数组
    # timeArray = time.strptime(now_time,'%Y-%m-%d %H:%M:%S')
    # now_TimeStamp = int(time.mktime(timeArray) * 1000)  # 毫秒转换
    return now_time

# 入库
def inStorage(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
	"action": 150,
    # "action": 371,
	"weight": 0.186,
    "volumeWeight": 13,
    "chargeableWeight": 23,
	"scanTime": get_now_time(),
    "stotageTime": get_now_time(),
	"timeZone": 8,
	"sourceCode": "ALLJOY",
	"countryCode": "KE",
	"storageCode": "20220106",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}

    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    channel = "MAPH"
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
            "countryCode": "KE",
            "trackingNumber": mailNo,
            "action": "181",
            "jobNumber": "CMN00012",
            "scanTime": get_now_time(),
            "timezone": 8,
            "weight": 0.34,
            "volumeWeight": 13,
            "chargeableWeight":23,
            "boxWeight": 0.1,
            "length": 0.00,
            "width": 0.00,
            "height": 0.00,
            # "packageCode": channel + str(random.randint(111111111111,999999999999)),
            "packageCode": "MAPH389175692365",
            "asnCode": "CMNGZ0120220617000008",
            "storageCode": "8600272206161886",
            "sourceCode": "MSD",
            "shipType":"ST04",
          "taxMethod":"DDP",
          "warehouseCode":"GZ01"
        }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    data = {
	"action": 190,
	"weight": 0.268,
	"asnCode": "CK0108SDF20220111018",
	"scanTime": "2022-12-11 17:52:44",
	"timeZone": 8,
	"sourceCode": "ALLJOY",
	"countryCode": "KE",
	"packageCode": "TH220111888",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    data = {
	"eta": "2022-01-12 06:00:00",
	"etd": "2022-01-11 06:00:00",
	"action": 191,
	"weight": 0.186,
	"asnCode": "CK0108SDF20220111018",
	"scanTime": "2022-12-11 18:03:31",
	"timeZone": 8,
	"sourceCode": "ALLJOY",
	"countryCode": "KE",
	"packageCode": "TH220111888",
	"storageCode": "20220106",
	"waybillCode": "ALLJOY0756",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    data = {
	"action": 220,
	"weight": 0.186,
	"asnCode": "CK0108SDF20220111018",
	"flightNo": "ALLJOY0756",
	"scanTime": "2022-12-11 18:10:40",
	"timeZone": 8,
	"flightDate": "2022-01-11 08:00:00",
	"sourceCode": "ALLJOY",
	"countryCode": "BD",
	"desPortCode": "GH",
	"packageCode": "TH220111888",
	"storageCode": "20220106",
	"waybillCode": "ALLJOY0756",    # 提单号
	"startPortCode": "HKG",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    data = {
	"action": 230,
	"weight": 0.186,
	"asnCode": "CK0108SDF20220111018",
	"flightNo": "ALLJOY0756",
	"landDate": "2022-01-12 08:28:30",
	"scanTime": "2022-12-11 18:18:03",
	"timeZone": 8,
	"sourceCode": "ALLJOY",
	"countryCode": "BD",
	"desPortCode": "BD",
	"packageCode": "BDPH380929130274",
	"waybillCode": "ALLJOY0756",
	"startPortCode": "HKG",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    data = {
	"eta": "2022-01-12 06:00:00",
	"etd": "2022-01-11 06:00:00",
	"action": 402,
	"weight": 0.186,
	"asnCode": "CK0108SDF20220111018",
	"scanTime": "2022-12-11 17:03:31",
	"timeZone": 8,
	"sourceCode": "ALLJOY",
	"countryCode": "KE",
	"packageCode": "TH220111888",
	"storageCode": "20220106",
	"waybillCode": "ALLJOY0756",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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
    data = {
	"action": 360,
	"weight": 0.186,
	"asnCode": "CK0108SDF20220111018",
	"scanTime": "2022-12-11 18:29:01",
	"timeZone": 8,
	"sourceCode": "ALLJOY",
	"countryCode": "UG",
	"packageCode": "TH220111888",
	"waybillCode": "ALLJOY0756",
	"trackingNumber": mailNo
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/alljoy/track/callback?appCode={appCode}&timestamp={timeline}"
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

    mailNo = "KE120000000222"
    # uat_config = "http://112.74.53.147:8480"
    uat_config = "https://apis.speedaf.com"
    # uat_config = "http://8.214.27.92:8480"


    inStorage(mailNo,uat_config)  #入库
    time.sleep(2)
    Package(mailNo,uat_config) #集包
    time.sleep(2)
    OUT_STORAGE(mailNo,uat_config)#出库
    time.sleep(2)
    INLAND_CONNECT(mailNo,uat_config)#国内交接完成
    time.sleep(2)
    CUSTOMS_CLEARANCE(mailNo, uat_config)  # 报关
    time.sleep(2)
    # FLIGHT(mailNo,uat_config)  #航班起飞
    # time.sleep(2)
    # LAND(mailNo,uat_config)  # 航班降落
    # time.sleep(2)
    # CUSTOMS(mailNo,uat_config)  # 清关中
    # time.sleep(2)







