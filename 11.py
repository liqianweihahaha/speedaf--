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
def createOrder():
    timeline = str(int((time.time() + 0.5) * 1000))
    data = {
        "acceptAddress": "SIDI MAAR2OUF 32L11OTISSEMENT COMMUNAL",
        "acceptCityCode": "C034",
        "acceptCityName": "Accra322 1W1est",
        "acceptCompanyName": "acceptCompanyName",
        "acceptCountryCode": "MA",
        "acceptCountryName": "Morocco",
        "acceptDistrictCode": "A0624",
        "acceptDistrictName": "ewe322eqewq11",
        "acceptEmail": "123@Test.com",
        "acceptMobile": "6666322365811",
        "acceptName": "lqw623662654811",
        "acceptPhone": "zc001",
        "acceptPostCode": "acceptCode",
        "acceptProvinceCode": "R006",
        "acceptProvinceName": "Gre111at2erAccra278887481",
        "codFee": 99.99,
        "customOrderNo": random.randint(1111111,9999999),
        "customerCode": "860061",  #uat测试客户
        # "customerCode": "860076",  # 线上测试客户
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
                        "goodsMaterial": "",
                        "goodsName": "item mane",
                        "goodsNameDialect": "item namme",
                        "goodsQTY": 2,
                        "goodsRemark": "goodsRemark",
                        "goodsRule": "goodsRule",
                        "goodsType": "IT01",
                        "goodsUnitPrice": 1,
                        "goodsValue": 100,
                        "currencyType": "USD",
                        "goodsWeight": 1.45,
                        "goodsHigh": 100,
                        "goodsLength": 200,
                        "goodsVolume": 1.52,
                        "makeCountry": "makeCountry",
                        "salePath": "salePath",
                        "sku": "sku001",
                        "unit": "",
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
        "deliveryType": "DE01",
        "payMethod": "PA01",
        "parcelType": "PT01",
        "shipType":"ST02",   # 区分本地件和国际件标识
        "transportType":"TT03",
        "platformSource":"csp",
        # "smallCode": random.randint(1111111,9999999),
        "threeSectionsCode": ""
}

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    url = f"http://8.214.27.92:8480/open-api/express/order/createOrder?appCode={appCode}&timestamp={timeline}"
    res = requests.post(url, data=myData, headers=headers,verify=False)

    re = json.loads(res.text)
    # print(re)

    if re['data'] != None:

        aa = DesUtils.triple_des_decrypt(re['data']).decode('utf-8')  # byte类型转字符串，先解码
        billCode = json.loads(aa)['billCode']  # 字符串类型转成字典类型,获取到运单号
        customerOrderNo = json.loads(aa)['customerOrderNo']   # 获取到客户单号
        print(f"下单成功，运单号为 {billCode},客户单号为 {customerOrderNo}")
        return billCode,customerOrderNo

    else:
        print(re)


# i = 0
# while i < 5:
createOrder()
    # i = i + 1

# print('Good bye!')