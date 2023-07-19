import requests
import json,time,random
import DesUtils
import pprint

# 创建菜鸟订单
def createCaiNiaoOrder():

    number = random.randint(1111111, 9999999)
    trcking_number = "xltest" + str(number)   # 运单号

    categoryFeature = random.choice(['00','02'])  # 物品类型

    logistics_interface1 = '''
    {
    "trade":{
        "tradeID":"%s"
    },
    "parcel":{
        "price":"1",
        "weight":"1000",
        "bigBagID":"SPA00000101R",
        "goodsList":[
            {
                "url":"http://www.aliexpress.com/item//4000000039670.html",
                "name":"Skirts",
                "price":"444",
                "cnName":"半身裙",
                "weight":"100",
                "quantity":"1",
                "itemPrice":"0",
                "priceUnit":"YUAN",
                "productID":"4000000039670",
                "categoryID":"349",
                "weightUnit":"g",
                "categoryName":"Skirts",
                "declarePrice":"12",    
                "priceCurrency":"USD",
                "securityLevel":"WHITE",
                "categoryCNName":"半身裙",
                "categoryFeature":"00",
                "productCategory":"Womens Clothing|Skirts",
                "suggestedCNName":"半身裙",
                "suggestedENName":"Skirts",
                "securityLogisticsAttributes":"ALL BATTERY"
            }
        ],
        "priceUnit":"CENT",
        "weightUnit":"g",
        "bigBagWeight":"1200",
        "parcelQuantity":"1",
        "suggestedWeight":"20",
        "parcelInspection":"WHITE_NORMAL"
    },
    "sender":{
        "imID":"aliqatest01",
        "name":"cx test",
        "phone":"13800000000",
        "address":{
            "city":"shen zhen shi",
            "country":"China",
            "district":"fu tian qu",
            "province":"guang dong sheng",
            "detailAddress":"hua qiang bei jie dao~~~Room 101, building 7,Hongli Village"
        },
        "zipCode":"518000",
        "storeName":"Shop402172 Store"
    },
    "bizType":"AE_4PL_STANDARD",
    "customs":{
        "declarePriceTotal":"1"
    },
    "laneCode":"L_AE_STANDARD_SPEEDAF",
    "receiver":{
        "imID":"aliqatest01",
        "name":"IUI545UI",
        "email":"testchenxi@gmail.com",
        "phone":"31-",
        "mobile":"4333434",
        "address":{
            "city":"545435",
            "country":"KE",
            "district":"5434",
            "province":"344",
            "detailAddress":"SIDI 435 LOTISSEMENT COMMUNAL "
        },
        "zipCode":"7102 DR"
    },
    "sortCode":"Africa",
    "tradeList":[

    ],
    "preCPResCode":"TRAN_STORE_30545263",
    "returnParcel":{
        "imID":"aliqatest01",
        "name":"asdfsdf",
        "phone":"18888888888",
        "mobile":"18888888888",
        "address":{
            "city":"亳州市",
            "country":"中国",
            "district":"利辛县",
            "province":"安徽省",
            "detailAddress":"城关镇~~~我Hi地方打xxx"
        },
        "zipCode":"123456",
        "undeliverableOption":"3"
    },
    "routingTrial":"1",
    "isMorePackage":"N",
    "nextCPResCode":"GATE_30522183",
    "interCPResCode":"GATE_30522183",
    "trackingNumber":"%s",
    "currentCPResCode":"TRUNK_30522182",
    "logisticsOrderCode":"%s",
    "logisticsOrderCreateTime":"2021-09-10 17:51:10"
    }
    '''%(trcking_number,trcking_number,trcking_number)

    # print(logistics_interface1)

    headers = {'content-type': 'application/x-www-from-urlencoded'}
    param = {'logistics_interface': logistics_interface1,'data_digest': "345343"}
    url = "http://8.214.27.92:8480/open-api/cainiao/order/asn"
    res = requests.post(url, params=param,headers=headers,verify=False)

    re = json.loads(res.text)
    print(re)

i = 0
while i < 25:
    re = createCaiNiaoOrder()
    # print(re)
    i = i + 1

print('Good bye!')
