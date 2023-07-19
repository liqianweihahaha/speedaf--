"""
思路：1-单个下单，并将运单号和客户单号return
"""

import requests
import json,time,random
import DesUtils
import pprint


appCode = "888888"
secretKey = "hvmaYYOyegNy4muv"

# appCode = "TT660020"
# secretKey = "kIPdsDXd"


# 下单接口
def createOrder(config):
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
        "acceptAddress": "4324UYUYI234",
        "acceptCityCode": "C034",
        "acceptCityName": "534RWERWERW5345",
        "acceptCompanyName": "acceptCompanyName",
        "acceptCountryCode": "MA",
        "acceptCountryName": "Morocco",
        "acceptDistrictCode": "A0624",
        "acceptDistrictName": "432TRETE32",
        "acceptEmail": "123@Test.com",
        "acceptMobile": "20220425115",
        "acceptName": "lqw20220425",
        "acceptPhone": "zc001",
        "acceptPostCode": "acceptCode",
        "acceptProvinceCode": "R006",
        "acceptProvinceName": "etst34343355",
        "codFee": 0,
        # "billCode": 7690000000000,
        "customOrderNo": random.randint(1111111,9999999),
        "customerCode": "860079",  #uat希音-推msd
        # "customerCode": "860062",   # uat普通客户--推msd
        # "customerCode": "860078",  # uat柒剑阿联酋-推msd
        # "customerCode": "860077",  # uat柒剑-推msd
        # "customerCode": "860076",  # uat亚洲创新-推msd

        # "customerCode": "860002",  # 线上测试客户
        "parcelHigh": 1000,
        "parcelLength": 1000,
        "parcelVolume": 1.52,
        "parcelWeight": 2.54,
        "parcelWidth": 1000,
        "goodsQTY": 2,
        "insurePrice": 875,
        "itemList": [
                {
                        "battery": 0,
                        "blInsure": 0,
                        "dutyMoney": 1000,
                        "goodsId": "19999",
                        "goodsName": "itemmanee",
                        "goodsNameDialect": "itemnam",
                        "goodsQTY": 3,
                        "goodsRemark": "goodsRemark",
                        "currencyType": "USD",
                        "goodsRule": "goodsRule",
                        "goodsType": "IT01",
                        "goodsUnitPrice": 1,
                        "goodsValue": 135,
                        "goodsWeight": 1.45,
                        "goodsHigh": 100,
                        "goodsLength": 200,
                        "goodsVolume": 1.52,
                        "makeCountry": "makeCountry",
                        "salePath": "salePath",
                        "sku": "sku001",
                        "unit": "yuan",
                        "goodsWidth": 200
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
        "payMethod": "PA01",
        "parcelType": "PT01",
        "shipType":"ST02",   # 区分本地件和国际件标识
        "transportType":"TT02",
        "platformSource":"csp",
        "smallCode": random.randint(1111111,9999999),
        "threeSectionsCode": ""
}

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

uat_config = "http://8.214.27.92:8480"

i = 0
while i < 8:
    createOrder(uat_config)
    # print(re)
    i = i + 1

print('Good bye!')
