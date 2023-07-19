"""
思路：1-单个下单，并将运单号和客户单号return
"""

import requests
import json,time,random
import DesUtils
import pprint

appCode = "888888"
secretKey = "hvmaYYOyegNy4muv"



# 下单接口
def createOrder(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
        "acceptAddress": "4324UYUYI234",
        "ACCEPT_STREET_NAME":"34234234",   # 新增字段，收件人街道（150和180，包括汇总面单，打单接口）
        "acceptCityCode": "C034",
        "acceptCityName": "534RWERWERW5345",
        "acceptCompanyName": "acceptCompanyName",
        "acceptCountryCode": "BD",
        "acceptCountryName": "The United Arab Emirates",
        "acceptDistrictCode": "A0624",
        "acceptDistrictName": "432TRETERTRET4234",
        "acceptEmail": "123@Test.com",
        "acceptMobile": "+2340000",  # 主手机号，必填
        # "acceptCitizenId":"11111111110",  #身份证id--土耳其
        "acceptName": "wewqeqwerewrewrwrrewrwer",
        "acceptPhone": "2341111111111",  # 备用手机号，选填
        "acceptPostCode": "acceptCode",
        "acceptProvinceCode": "R006",
        "acceptProvinceName": "  3456REWR 7899 5501  ",
        "codFee": 10,
        # "billCode": 666666664,
        "customOrderNo": random.randint(1111111,9999999),
        # "customerCode": "CN000011",   # uat普通客户--推msd
        # "customerCode": "8800035",  # 测试环境
        # "customerCode": "BD000068",  # 芬奇国际---推msd

        "customerCode": "BD000066",  # uat柒剑阿联酋-推msd
        # "customerCode": "860077",  # uat柒剑-推msd
        # "customerCode": "860076",  # uat亚洲创新-推msd

        # "customerCode": "860002",  # 线上测试客户
        "parcelHigh": 1000,
        "parcelLength": 1000,
        "parcelVolume": 1.52,
        "parcelWeight": 0,
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
                "goodsName": "itemmanee",
                "goodsNameDialect": "itemnam",
                "goodsQTY": 3,  # 商品数量
                "goodsRemark": "goodsRemark",
                "goodsRule": "goodsRule",
                "goodsType": "IT01",
                "goodsUnitPrice": 1,
                "goodsValue": 10,  # 商品申报价值
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
                "goodsValue": 10,  # 商品申报价值
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
            }
        ],
        "piece": 1,
        "remark": "1",
        "sendAddress": "sendAddre",
        "sendCityCode": "sendCityCode",
        "sendCityName": "sendCityName",
        "sendCompanyName": "sendCompanyName",
        "sendCountryCode": "CN",
        "sendCountryName": "China",
        "sendDistrictCode": "sendDistrictCode",
        "sendDistrictName": "sendDistrictName",
        "sendMail": "sendMail",
        "sendMobile": "sendMobile",
        "sendName": "sendName",
        "sendPhone": "sendPhone",
        "sendPostCode": "sendPostCode",
        "sendProvinceCode": "sendProvinceCode",
        "sendProvinceName": "sendProvinceName",
        "shippingFee": 1,
        "deliveryType": "DE02",
        "payMethod": "PA01",  # PA01 现金
        "parcelType": "PT01",
        "shipType":"ST02",   # 区分本地件 ST01 和国际件 ST02  海外仓发 ST03标识
        "transportType":"TT02",
        "platformSource":"csp",
        "smallCode": random.randint(1111111,9999999),
        "threeSectionsCode": ""
}

    myData = DesUtils.triple_des_encrypt(data, timeline)

    # print(data,myData)  # 加密前和加密后的请求体



    headers = {'content-type': 'application/json'}
    url = config + f"/open-api/express/order/createOrder?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers, verify=False)

    re = json.loads(res.text)
    # print(re)  # 加密后的响应数据

    if re['data'] != None:

        aa = DesUtils.triple_des_decrypt(re['data']).decode('utf-8')  # byte类型转字符串，先解码
        # print(aa) # 解密后的响应数据

        billCode = json.loads(aa)['billCode']  # 字符串类型转成字典类型,获取到运单号

        customerOrderNo = json.loads(aa)['customerOrderNo']  # 获取到客户单号
        print(f"下单成功，运单号为 {billCode},客户单号为 {customerOrderNo}")
        return billCode, customerOrderNo

    else:
        print(re)


# 集包
def Package(mailNo,config):
    channel = "MAPH"
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
            "countryCode": "GH",
            "trackingNumber": mailNo,
            "action": "181",
            "jobNumber": "CMN00012",
            "scanTime": "2022-06-21 08:17:37",
            "timezone": 8,
            "weight": 0.34,
            "boxWeight": 0.1,
            "length": 0.00,
            "width": 0.00,
            "height": 0.00,
            "packageCode": "BDPH296511945131",
            "asnCode": "CMNGZ0120220617000008",
            "storageCode": "8600272206161886",
            "sourceCode": "MSD",
            # "shipType":"ST04",
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



# 航班起飞
def FLIGHT(mailNo,config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
	"action": 220,
	"weight": 0.186,
	"asnCode": "CK0108SDF20220111018",
	"flightNo": "test001",   # 航班号
	"scanTime": "2022-01-11 18:10:40",
	"timeZone": 8,
	"flightDate": "2022-01-11 08:00:00",
	"sourceCode": "MSD",
	"countryCode": "BD",
	"desPortCode": "BD",
	"packageCode": "BDPH296511945131",   # 箱号
	"storageCode": "test001",
    "waybillCode": "TEST20221114",  # 提单号
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






if __name__ == "__main__":
    # uat_config = "https://apis.speedaf.com/"
    # uat_config = "http://8.214.27.92:8480"
    uat_config = "http://112.74.53.147:8480"

    billCodeList = []
    # 1---openapi下单
    i = 0
    while i < 2:
        info = createOrder(uat_config)
        billCode = info[0]
        billCodeList.append(billCode)
        i = i + 1

    print('Good bye!')
    print(billCodeList)


  # 2--模拟敏思达推航班起飞轨迹
    for billCode in billCodeList:
        FLIGHT(billCode,uat_config)

    # for billCode in billCodeList:
    #     Package(billCode,uat_config)