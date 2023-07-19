"""
思路：1-单个下单，并将运单号和客户单号return
"""

import requests
import json,time,random
import DesUtils
import pprint

appCode = "888888"
secretKey = "hvmaYYOyegNy4muv"

# appCode = "2340002"
# secretKey = "jqhp5PAOPKFV9LpU"



# 下单接口
def createOrder(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    alphabet = 'abcdefghijklmnopqrstuvw3xyz234324234234324trtretretertert'
    data = {
        "isAllowOpen":'1',   # 是否允许打开包裹-埃及本地件
        "undeliverableOption":'2',  # 0=不处理 1=丢弃 2=退回
        "acceptAddress": 'E-5 Abrar Calony Kharian Cantt Pakistan',
        "taxMethod":"DDP",  # 税费方式 DDU、DDP
        "tax":"123",
        # "ACCEPT_STREET_NAME":"34234234",   # 新增字段，收件人街道（150和180，包括汇总面单，打单接口）
        "laneCode":"M",   # E是经济，R是标准，M是无忧简易，RS是标准特货，ES是经济特货    无=其他
        # "productService":"EP-C2G-YANWEN-E",  # 燕文包裹类型映射到 经济
        "acceptStreetName":'',
        # "acceptCityCode": "C034",
        "acceptCityName": 'Kharian cantt',
        "acceptCompanyName": "acceptCompanyName",
        "acceptCountryCode": "BD",
        "acceptCountryName": "",
        # "acceptDistrictCode": "A0624",
        "acceptDistrictName": '',
        "acceptEmail": "1127771903@qq.com",
        "acceptMobile":'4234234',  # 主手机号，必填
        # "acceptCitizenId":"11111111110",  #身份证id--土耳其
        "acceptName":'soyannwo fiyinfolu',
        "acceptPhone": '8033585699',  # 备用手机号，选填
        "acceptPostCode": "acceptCode",
        # "acceptProvinceCode": "R006",
        "acceptProvinceName": 'Pakistan Punjab',
        "codFee": 10,
        # "billCode": 'XKE1013578510',
        "customOrderNo": random.randint(1111111,9999999),
        # "customOrderNo": "246810",
        # "customerCode": "BD000081",   # uat普通客户--推msd
        "customerCode": "PK000408",  #fordeal 客户编号
        "currencyType": "USD",
        # "customerCode": "BD000070",  # 芬奇国际---推msd

        # "customerCode": "CN000094",  # uat柒剑阿联酋-推msd
        # "customerCode": "860077",  # uat柒剑-推msd
        # "customerCode": "860076",  # uat亚洲创新-推msd

        # "customerCode": "860002",  # 线上测试客户
        # "customerCode": "860025",
        # "customerCode":"860039",
        # "customerCode": "2120031",
        "parcelHigh": 1000,
        "parcelLength": 1000,
        "parcelVolume": 1.52,
        "parcelWeight": 2,
        "parcelWidth": 1000,
        "goodsQTY": 2,
        "insurePrice": 875,
        "itemList": [
            {
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee3234324234234",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 1,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT04",
                "goodsUnitPrice": 1,
                "goodsValue": 1999,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 10,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku00132432&^&6723213213213321",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },
            {
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 1,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 10,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 10,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },
            {
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 1,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },
            {
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },
            {
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },
            {
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },{
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },{
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },{
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },{
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },{
                "battery": 0,
                "blInsure": 0,
                "dutyMoney": 1000,
                "goodsId": "19999",
                "goodsMaterial": "",
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 30,  # 商品申报价值
                "currencyType": "USD",
                "goodsWeight": 0,  # 商品重量
                "goodsHigh": 100,
                "goodsLength": 200,
                "goodsVolume": 1.52,
                "makeCountry": "makeCountry",
                "salePath": "salePath",
                "sku": "sku001",
                "unit": "",
                "goodsWidth": 200,
                "hsCode": "234324234"
            },
        ],
        "piece": 1,
        "remark": "1",
        "sendAddress": "~~~B607 Resplendence Mansion, No.381, Kangli Road, Libeiling county",
        "sendCityCode": "sendCityCode",
        "sendCityName": "dong guan shi",
        "sendCompanyName": "sendCompanyName",
        "sendCountryCode": "CN",
        "sendCountryName": "China",
        "sendDistrictCode": "sendDistrictCode",
        "sendDistrictName": "da lang zhen",
        "sendMail": "sendMail",
        "sendMobile": '18929130752',
        "sendName": "Shen Wenyang一二三四五六七八九十一二三四五六七八九十23432432",
        "sendPhone": '18929130752',
        "sendPostCode": "sendPostCode",
        "sendProvinceCode": "sendProvinceCode",
        "sendProvinceName": "guang dong sheng",
        "shippingFee": 1,
        "deliveryType": "DE01",   # DE01--派送上门  DE02--自提
        "pickupType": 2,   # 1代表上门揽收（走分单模块）    2代表客户自送
        "payMethod": "PA02",  # PA01 现金
        "parcelType": "PT01",
        "shipType":"ST02",   # 区分本地件 ST01 和国际件 ST02  海外仓发 ST03标识
        "transportType":"TT01",
        "platformSource":"csp",
        "smallCode": random.randint(1111111,9999999),
        "threeSectionsCode": ""
}

#     data = {
#         "acceptAddress": "acceptAddress",
#         "acceptCityCode": "acceptCityCode",
#         "acceptCityName": "acceptCityName",
#         "acceptCompanyName": "acceptCompanyName",
#         "acceptCountryCode": "TR",
#         "acceptCountryName": "Nigiera",
#         "acceptDistrictCode": "acceptDistrictCode",
#         "acceptDistrictName": "acceptDistrictName",
#         "acceptEmail": "123@Test.com",
#         "acceptMobile": "1778922222",
#         "acceptName": "acceptName",
#         "acceptPhone": "999999",
#         "acceptPostCode": "acceptPostCode",
#         "acceptProvinceCode": "acceptProvinceCode",
#         "acceptProvinceName": "acceptProvinceName",
#         "codFee": 100,
#         "customOrderNo": random.randint(1111111,9999999),
#         "customerCode": "TR000002",  # 希音土耳其客户账号--测试环境、uat环境
#         # "customerCode": "CN000095",  # uat普通客户--推msd
#         "parcelHigh": 1000,
#         "parcelLength": 1000,
#         "parcelVolume": 1.52,     # 体积
#         "parcelWeight": 2.54,     # 毛重
#         "parcelWidth": 1000,
#         "goodsQTY": 2,
#         "insurePrice": 875,
#         "itemList": [{
#                 "battery": 0,
#                 "blInsure": 0,
#                 "dutyMoney": 1000,
#                 "goodsId": "19999",
#                 "goodsMaterial": "",
#                 "goodsName": "item mane",
#                 "goodsNameDialect": "item namme",
#                 "goodsQTY": 2,
#                 "goodsRemark": "goodsRemark",
#                 "goodsRule": "goodsRule",
#                 "goodsType": "IT02",
#                 "goodsUnitPrice": 1,
#                 "goodsValue": 190,
#                 "goodsWeight": 1.45,
#                 "goodsHigh": 100,
#                 "goodsLength": 200,
#                 "goodsVolume": 1.52,
#                 "makeCountry": "makeCountry",
#                 "salePath": "salePath",
#                 "sku": "sku001",
#                 "unit": "",
#                 "goodsWidth": 200
#         }],
#         "piece": 1,
#         "remark": "1",
#         "sendAddress": "sendAddress",
#         "sendCityCode": "sendCityCode",
#         "sendCityName": "sendCityName",
#         "sendCompanyName": "sendCompanyName",
#         "sendCountryCode": "TR",
#         "sendCountryName": "Turkey",
#         "sendDistrictCode": "sendDistrictCode",
#         "sendDistrictName": "sendDistrictName",
#         "sendMail": "sendMail",
#         "sendMobile": "sendMobile",
#         "sendName": "sendName",
#         "sendPhone": "sendPhone",
#         "sendPostCode": "sendPostCode",
#         "sendProvinceCode": "sendProvinceCode",
#         "sendProvinceName": "sendProvinceName",
#         "shippingFee": 1,
#         "deliveryType": "DE01",
#         "payMethod": "PA01",
#         "parcelType": "PT01",
#         "shipType": "ST01",
#         "transportType": "TT01",
#         "platformSource": "Ebeano",
#         "smallCode": "box",
#         "threeSectionsCode": "",
#         # "pickupBatch": random.randint(44444444444,99999999999)
#         "pickupBatch": "93855128988"
# }


    myData = DesUtils.triple_des_encrypt(data, timeline)


    # print(data,myData)  # 加密前和加密后的请求体

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/order/createOrder?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    re = json.loads(res.text)
    # print(re)  # 加密后的响应数据

    if re['data'] != None:

        aa = DesUtils.triple_des_decrypt(re['data']).decode('utf-8')  # byte类型转字符串，先解码
        # print(aa) # 解密后的响应数据

        billCode = json.loads(aa)['billCode']  # 字符串类型转成字典类型,获取到运单号
        customerOrderNo = json.loads(aa)['customerOrderNo']   # 获取到客户单号
        print(f"下单成功，运单号为 {billCode},客户单号为 {customerOrderNo}")
        return billCode,customerOrderNo

    else:
        print(re)


# 打印面单
def printFace(config,billCode,labelType):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
    "waybillNoList": [
        billCode
        # 86212220294055
    ],
    "labelType": labelType      # 1=三联单 2=不带logo两联单 3=带logo两联单   5=两联单100*150  6=两联单100*150汇总   7=嘀咑购ETSG
    }
    # print('面单加密前的请求体：',data)

    myData = DesUtils.triple_des_encrypt(data,timeline)
    # print('面单加密后的请求体：', myData)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/order/print?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)
    # print('面单解密前的响应体：', res)

    re = json.loads(res.text)

    if re['data'] != None:
        aa = DesUtils.triple_des_decrypt(re['data']).decode('utf-8')
        # print('面单解密后的响应体：', aa)
        labelBase64 = json.loads(aa)['orderLabels'][0]['labelBase64']

        if labelBase64 != '':
            print('运单号打印成功')
            print(DesUtils.triple_des_decrypt(re['data']))
        else:
            print('打印失败，labelBase64为空')
    else:
        print(re)


# 轨迹订阅回调
def  trackCallBack(config,billCode):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
        "mailNo": billCode,
        "customerCode": "2340002",
        "notifyUrl": config + "/open-api/express/track/callback"
    }

    myData = DesUtils.triple_des_encrypt(data, timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/subscribe?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    re = json.loads(res.text)
    # print(re)

    if re['success']  == True:
        print(f"运单号:{billCode}轨迹订阅回调成功")
    else:
        print("轨迹订阅回调失败")


# k9轨迹推送
def trackPush(config,billCode):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
    "mailNo": billCode,
    "action": "1",
    "actionName": "收件",
    "message": "【Test A】已做收件扫描，收件员是【Test A】【08033689240】",
    "msgEng": "【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc": "【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "time": "2021-01-21 13:40:28",
    "timezone": 8,
    "country": "Nigeria",
    "countryCode": "NG",
    "sourceCode":"K9",
    "optCode":"86001",
    "optName":"jack",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "weight":1
},{
    "mailNo": billCode,
    "action": "2",
    "actionName": "发件",
    "message": "【Test A】已做发件扫描，发件员是【Test A】【08033689240】",
    "msgEng": "【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "msgLoc": "【Test B】scanned for delivery;The courier is 【Ade Test B】【08055598166】",
    "time": "2021-01-21 13:44:28",
    "timezone": 8,
    "country": "Nigeria",
    "countryCode": "NG",
    "sourceCode":"K9",
    "optCode":"86001",
    "optName":"jack",
    "packageCode":"1002928",
    "storageCode":"2928280",
    "ladingBillCode":"02828220",
    "weight":1
}]

    mydata = DesUtils.triple_des_encrypt(data,timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/push?appCode={appCode}&timestamp={timeline}"
    re = requests.post(url,data=mydata,headers=headers,verify=False)

    re = json.loads(re.text)

    if re["success"] == True:
        print(f"运单号: {billCode} k9轨迹推送接口正常")
    else:
        print("k9轨迹推送接口失败")

# 轨迹实时查询
def trackQuery(config,billCode):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
    "mailNoList": [billCode]
    }

    mydata = DesUtils.triple_des_encrypt(data,timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/track/query?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url,data=mydata,headers=headers,verify=False)

    re = json.loads(res.text)

    if re["success"] == True:
        print(f"运单号：{billCode} 实时轨迹正常查询")
        track = DesUtils.triple_des_decrypt(re["data"])
        print(f"轨迹数据：{track}")
    else:
        print("实时轨迹查询失败")


# 根据地址获取三段码
def getThreeSectionsCodeByAddress(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
    "countryCode":"NG",
    "provinceName":"Abuja",
    "cityName":"Maitama",
    "distinctName":"",
    "address":"Dumez Building, Plot 3120 Rima Street, Off Gu"
    }

    mydata = DesUtils.triple_des_encrypt(data, timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/network/threeSectionsCode/getByAddress?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=mydata, headers=headers,verify=False)

    re = json.loads(res.text)

    if re["success"] == True:
        print(f"根据地址查询三段码接口--正常")
        data = DesUtils.triple_des_decrypt(re["data"])
    else:
        print("根据地址查询三段码接口--失败")


# 根据运单号查询三段码
def getThreeSectionsCodeByBillCode(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
    "billCode":"47254200594964"
    }

    mydata = DesUtils.triple_des_encrypt(data, timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/network/threeSectionsCode/getByBillCode?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=mydata, headers=headers,verify=False)

    re = json.loads(res.text)

    if re["success"] == True:
        print(f"根据运单号查询三段码接口--正常")
        data = DesUtils.triple_des_decrypt(re["data"])
        print(data)
    else:
        print("根据运单号查询三段码接口--失败")


# 根据国家编码查询树形结构地区数据
def getAreaTree(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
        "countryCode": "CN"
    }

    mydata = DesUtils.triple_des_encrypt(data,timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/common/area/getAreaTree?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=mydata, headers=headers,verify=False)

    re = json.loads(res.text)
    if re["success"] == True:
        print("根据国家编码查树形结构--正常")
        data = DesUtils.triple_des_decrypt(re["data"])
        pprint.pprint(data)
    else:
        print("根据国家编码查树形结构--失败")

# 根据国家和父级编码查询下级地区
def getArea(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
    "countryCode":"CN",
    "parentCode":"R001",
    "type":2
    }

    mydata = DesUtils.triple_des_encrypt(data, timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/common/area/getAreaTree?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=mydata, headers=headers,verify=False)

    re = json.loads(res.text)
    if re["success"] == True:
        print("根据国家和父级编码查询下级地区--正常")
    else:
        print("根据国家和父级编码查询下级地区--失败")


# 更新订单接口
def updateOrder(config,billCode):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [{
        "billCode": billCode,
        "customerCode": "860025",
        "acceptAddress": "acceptAddress",
        "acceptCityCode": "acceptCityCode",
        "acceptCityName": "acceptCityName",
        "acceptCompanyName": "acceptCompanyName",
        "acceptDistrictCode": "acceptDistrictCode",
        "acceptDistrictName": "acceptDistrictName",
        "acceptEmail": "123@Test.com",
        "acceptMobile": "1778922222",
        "acceptName": "lqw",
        "acceptPhone": "999999",
        "acceptPostCode": "acceptPostCode",
        "acceptProvinceCode": "acceptProvinceCode",
        "acceptProvinceName": "acceptProvinceName",
        "codFee": 9999999.99,
        "parcelHigh": 1000,
        "parcelLength": 1000,
        "goodsQTY": 99,
        "parcelVolume": 1,
        "parcelWeight": 200,
        "parcelWidth": 1000,
        "insurePrice": 876,
        "piece": 1,
        "remark": "1",
        "sendAddress": "sendAddress",
        "sendCityCode": "sendCityCode",
        "sendCityName": "sendCityName",
        "sendCompanyName": "sendCompanyName",
        "sendDistrictCode": "sendDistrictCode",
        "sendDistrictName": "sendDistrictName",
        "sendMail": "sendMail",
        "sendMobile": "sendMobile",
        "sendName": "yyyyyyyyyyyyy-修改后的",   # 寄件人姓名
        "sendPhone": "sendPhone",
        "sendPostCode": "sendPostCode",
        "sendProvinceCode": "sendProvinceCode",
        "sendProvinceName": "sendProvinceName",
        "shippingFee": 1,
        "deliveryType": "DE01",
        "payMethod": "PA01",
        "shipType":"ST01",
        "transportType":"TT01",
        "smallCode": ""
}]

    mydata = DesUtils.triple_des_encrypt(data, timeline)
    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/order/updateOrder?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=mydata, headers=headers,verify=False)

    re = json.loads(res.text)
    if re["success"] == True:
        print(f"运单号：{billCode} 更新成功")
    else:
        print("更新失败")

# 取消订单
def cancelOrder(config,billCode):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = [
    {
        "customerCode":"860059",
        "billCode":billCode,
        "cancelReason":"客户取消发货",
        "cancelBy":"TONY",
        "cancelTel":"135xxxx1029"
    }
   ]

    # print('加密前的请求体',data)

    mydata = DesUtils.triple_des_encrypt(data, timeline)

    # print('加密后的请求体',mydata)

    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/order/cancelOrder?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=mydata, headers=headers,verify=False)

    # print('取消接口返回体：',res)

    re = json.loads(res.text)
    if re["success"] == True:
        print(f"运单号：{billCode} 取消成功")
    else:
        print("取消失败")



if __name__ == "__main__":
    # uat_config = "http://47.241.40.42:8480"
    # uat_config = "https://apis.speedaf.com/"
    # uat_config = "http://47.241.92.41:8480"
    # uat_config = "http://8.214.27.92:8480"
    uat_config = "http://112.74.53.147:8480"



    # 1---openapi下单
    i = 0
    while i < 1:
        info = createOrder(uat_config)
        billCode = info[0]
        i = i + 1
    #
    print('Good bye!')



    # customerOrderNo = info[1]
    # time.sleep(10)

    # 2---openapi打印面单
    printFace(uat_config,billCode,2)   # 1=三联单 2=不带logo两联单 3=带logo两联单   5=两联单100*150  6=两联单100*150汇总   7=嘀咑购ETSG
    time.sleep(1)


    # # 3---轨迹订阅回调
    # trackCallBack(uat_config,billCode)
    #
    # # 4---k9轨迹推送
    # trackPush(uat_config,billCode)
    # time.sleep(10)
    #
    #
    # # 5---轨迹实时查询
    # trackQuery(uat_config,billCode)
    # time.sleep(10)


    # 6---根据地址获取三段码
    # getThreeSectionsCodeByAddress(uat_config)

    # 7---根据运单号获取三段码
    # getThreeSectionsCodeByBillCode(uat_config)

    # 8---根据国家编码查询树形结构地区数据
    # getAreaTree(uat_config)

    # 9---根据国家和父级编码查询下级地区
    # getArea(uat_config)

    # 10---更新订单
    # billCode = "BD020156553716"
    # updateOrder(uat_config,billCode)

    # 11---取消订单
    # billCode = "GH120000004866"
    # cancelOrder(uat_config,billCode)




