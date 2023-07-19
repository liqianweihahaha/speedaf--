import requests
import json

uat_url = "http://47.241.40.42:8480/open-api/wish/order/asn"

payload = {
    "otype":"8551-1",
    "sname":"GD_USPS_FC",
    "stype":1,
    "apiKey":"B2QoiMnuzjP7KrvI",
    "isTest":True,
    "parcel":{
        "weight":0.45,
        "priceUnit":"dollar",
        "categoryEn":"",
        "hasBattery":False,
        "weightUnit":"kg",
        "productList":[
            {
                "sku":"561f48726475cc5873cda03e",
                "value":1.23,
                "weight":1,
                "imageUrl":"https://www.wish.com/c/561f48726475cc5873cda03e",
                "quantity":1,
                "categoryEn":"",
                "hasBattery":False,
                "descriptionEn":"Yoga pants",
                "originCountry":"CN",
                "descriptionLocal":"瑜伽裤",
                "originCountryCode":"CHZ"
            }
        ],
        "declareValue":1.2,
        "descriptionEn":"Yoga pants",
        "dimensionUnit":"cm",
        "priceCurrency":"usd",
        "descriptionLocal":"瑜伽裤",
        "intrinsic_value":"11"
    },
    "pickUp":{
        "phone":"13763813216",
        "mobile":"",
        "addressEn":{
            "city":"Zhongshanshi",
            "name":"Zhoushisen",
            "country":"China",
            "province":"Guangdongsheng",
            "streetAddress1":"Guangdongshengzhongshanshisanjiaozhenjinsandadaodongsanshijiuhaozhiyililangdacangku（chengtaiduimian）"
        },
        "countryCode":"CHN",
        "addressLocal":{
            "city":"中山市",
            "name":"周世森",
            "country":"中国",
            "province":"广东省",
            "streetAddress1":"广东省中山市三角镇金三大道东三十九号之一利朗达仓库（诚泰对面）"
        }
    },
    "sender":{
        "phone":"15989136708",
        "mobile":"15989136708",
        "email":"",
        "zipCode":"310000",
        "addressEn":{
            "city":"Shenzhen",
            "name":"Baiying shenzhen trading company limited",
            "country":"China",
            "province":"Guangdong",
            "streetAddress1":"Floor 5, building a, no.10 of east area weikangde industrial park shangxue technology city longgang"
        },
        "countryCode":"CHN",
        "addressLocal":{
            "city":"Shenzhen",
            "name":"BAIYING SHENZHEN TRADING COMPANY LIMITED",
            "country":"中国",
            "province":"Guangdong",
            "streetAddress1":"Floor 5, Building A, No.10 of East Area Weikangde Industrial Park Shangxue Technology City Longgang"
        }
    },
    "isTaxed":False,
    "receiver":{
        "phone":"198308888",
        "mobile":"15989136708",
        "zipCode":"94016",
        "email":"123@qq.com",
        "addressEn":{
            "city":"San Francisco",
            "name":"Carlota lopez",
            "country":"Nigeria",
            "province":"CA",
            "streetAddress1":"54 ann st apt#1"
        },
        "countryCode":"NGA",
        "addressLocal":{
            "city":"San Francisco",
            "name":"Carlota Lopez",
            "country":"Nigeria",
            "province":"CA",
            "streetAddress1":"54 ann st apt#1"
        }
    },
    "carryType":2,
    "orderTime":"2018-05-31T12:45:30.962Z",
    "timestamp":"2018-06-01T03:41:13.285Z",
    "pickupType":1,
    "trackingId":"33333",
    "carrierCode":111,
    "requireLabel":False,
    "wishpostSname":"GD_USPS_FC",
    "paymentAccount":{
        "id":"591185160e36e6d296fbddaf",
        "email":"shiqi@wish.com",
        "username":"shiqi",
        "contactName":"shiqi",
        "phoneNumber":"12345",
        "merchantPayVat":False
    },
    "wishpostServiceType":"3PL",
    "wishpostBusinessType":"GENERAL_LOGISTICS",
    "source_warehouse":"1",
    "destination_warehouse":"1",
    "user_custom_description":"sss",
    "paid_with_wish":"true",
    "merchant_pay_vat":"false",
    "return_info":{
        "return_action_in_country":0,
        "return_action_out_country":0,
        "return_address_in_country":{
            "phone":"",
            "mobile":"",
            "country_code":"",
            "address_en":{
                "country":"",
                "province":"",
                "city":"",
                "name":"",
                "street_address1":""
            },
            "address_local":{
                "country":"",
                "province":"",
                "city":"",
                "name":"",
                "street_address1":""
            }
        },
        "return_address_out_country":{
            "phone":"",
            "mobile":"",
            "country_code":"",
            "address_en":{
                "country":"",
                "province":"",
                "city":"",
                "name":"",
                "street_address1":"hajhf"
            },
            "address_local":{
                "country":"",
                "province":"",
                "city":"",
                "name":"",
                "street_address1":""
            }
        }
    }
}


headers = {
  'Content-Type': 'application/json',
}

response = requests.post(uat_url, headers=headers, json=payload)
import pprint
pprint.pprint(response.text)

