"""
思路：1-下单：tracking_id随机生成，每次生成不同的 logistics_order_code
    2-取消订单：将下单接口中返回的 tracking_id 和 logistics_order_code 提取出来，参数引用到取消订单接口
    3-打印面单：将下单接口中返回的tracking_id 和 logistics_order_code 提取出来，参数引用到拉取面单接口
"""
import requests
import random,json


# wish下单接口
def create_order_wish(config):
    url = config + "/open-api/wish/order/asn"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "otype": "8551-1",
        "sname": "GD_USPS_FC",
        "stype": 1,
        "apiKey": "B2QoiMnuzjP7KrvI",
        "isTest": True,
        "parcel": {
            "weight": 0.45,
            "priceUnit": "dollar",
            "categoryEn": "",
            "hasBattery": False,
            "weightUnit": "kg",
            "productList": [
                {
                    "sku": "561f48726475cc5873cda03e",
                    "value": 1.23,
                    "weight": 1,
                    "imageUrl": "https://www.wish.com/c/561f48726475cc5873cda03e",
                    "quantity": 1,
                    "categoryEn": "",
                    "hasBattery": False,
                    "descriptionEn": "Yoga pants",
                    "originCountry": "CN",
                    "descriptionLocal": "瑜伽裤",
                    "originCountryCode": "CHZ"
                }
            ],
            "declareValue": 1.2,
            "descriptionEn": "Yoga pants",
            "dimensionUnit": "cm",
            "priceCurrency": "usd",
            "descriptionLocal": "瑜伽裤",
            "intrinsic_value": "11"
        },
        "pickUp": {
            "phone": "666",
            "mobile": "6665",
            "addressEn": {
                "city": "Zhongshanshi",
                "name": "Zhoushisen",
                "country": "China",
                "province": "Guangdongsheng",
                "streetAddress1": "Guangdongshengzhongshanshisanjiaozhenjinsandadaodongsanshijiuhaozhiyililangdacangku（chengtaiduimian）"
            },
            "countryCode": "CHN",
            "addressLocal": {
                "city": "中山市",
                "name": "周世森",
                "country": "中国",
                "province": "广东省",
                "district":"南山区",
                "streetAddress1": "广东省中山市三角镇金三大道东三十九号之一利朗达仓库（诚泰对面）"
            }
        },
        "sender": {
            "phone": "15989136708",
            "mobile": "15989136708",
            "email": "",
            "zipCode": "310000",
            "addressEn": {
                "city": "Shenzhen",
                "name": "Baiying shenzhen trading company limited",
                "country": "China",
                "province": "Guangdong",
                "streetAddress1": "Floor 5, building a, no.10 of east area weikangde industrial park shangxue technology city longgang"
            },
            "countryCode": "CHN",
            "addressLocal": {
                "city": "Shenzhen",
                "name": "BAIYING SHENZHEN TRADING COMPANY LIMITED",
                "country": "中国",
                "province": "Guangdong",
                "streetAddress1": "Floor 5, Building A, No.10 of East Area Weikangde Industrial Park Shangxue Technology City Longgang"
            }
        },
        "isTaxed": False,
        "receiver": {
            "phone": "198308888",
            "mobile": "15989136708",
            "zipCode": "94016",
            "email": "123@qq.com",
            "addressEn": {
                "city": "San Francisco",
                "name": "Carlota lopez",
                "country": "Nigeria",
                "province": "CA",
                "streetAddress1": "54 ann st apt#1"
            },
            "countryCode": "NGA",
            "addressLocal": {
                "city": "San Francisco",
                "name": "Carlota Lopez",
                "country": "Nigeria",
                "province": "CA",
                "streetAddress1": "54 ann st apt#1"
            }
        },
        "carryType": 2,
        "orderTime": "2018-05-31T12:45:30.962Z",
        "timestamp": "2018-06-01T03:41:13.285Z",
        "pickupType": 1,
        "trackingId": random.randint(1111111,9999999),   # 随机生成7位trackingId
        "carrierCode": 111,
        "requireLabel": False,
        "wishpostSname": "GD_USPS_FC",
        "paymentAccount": {
            "id": "591185160e36e6d296fbddaf",
            "email": "shiqi@wish.com",
            "username": "shiqi",
            "contactName": "shiqi",
            "phoneNumber": "12345",
            "merchantPayVat": False
        },
        "wishpostServiceType": "3PL",
        "wishpostBusinessType": "GENERAL_LOGISTICS",
        "source_warehouse": "1",
        "destination_warehouse": "1",
        "user_custom_description": "sss",
        "paid_with_wish": "true",
        "merchant_pay_vat": "false",
        "return_info": {
            "return_action_in_country": 0,
            "return_action_out_country": 0,
            "return_address_in_country": {
                "phone": "",
                "mobile": "",
                "country_code": "",
                "address_en": {
                    "country": "",
                    "province": "",
                    "city": "",
                    "name": "",
                    "street_address1": ""
                },
                "address_local": {
                    "country": "",
                    "province": "",
                    "city": "",
                    "name": "",
                    "street_address1": ""
                }
            },
            "return_address_out_country": {
                "phone": "",
                "mobile": "",
                "country_code": "",
                "address_en": {
                    "country": "",
                    "province": "",
                    "city": "",
                    "name": "",
                    "street_address1": "hajhf"
                },
                "address_local": {
                    "country": "",
                    "province": "",
                    "city": "",
                    "name": "",
                    "street_address1": ""
                }
            }
        }
    }
    re = requests.post(url,headers=headers,json=payload,verify=False)
    # print(type(re.text))  # 返回值是json格式
    re = json.loads(re.text)
    if re["message"] == "success":
        print(f"下单成功 ")
        print("订单号为：" + re["logistics_order_code"])
        print("tracking_id:" + re["tracking_id"])
        return re["logistics_order_code"], re["tracking_id"]  # 返回运单号和trackingId
    else:
        print("下单失败")


# 取消订单
def cancle_order(config,tracking_id,logistics_order_code):
    url = config + "/open-api/wish/order/cancel"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "api_key": "B2QoiMnuzjP7KrvI",
        "tracking_id": tracking_id,
        "logistics_order_code":logistics_order_code,
        "cancel_reason": "input incorrect receiver addressfsaf",
        "carry_type": "2",
    }
    re = requests.post(url,headers=headers,json=payload,verify=False)
    re = json.loads(re.text)
    if re["message"] == "Cancel successfully":
        print(f"{logistics_order_code},取消成功")
    else:
        print(f"{logistics_order_code},取消失败")


# 拉取面单
def getFetchLabel(config,tracking_id,logistics_order_code):
    url = config + "/open-api/wish/order/getFetchLabel"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "api_key": "B2QoiMnuzjP7KrvI",
        "tracking_id": tracking_id,
        "logistics_order_code": logistics_order_code,
    }
    re = requests.post(url,headers=headers,json=payload,verify=False)
    re = json.loads(re.text)
    if re["label_base64"] != "" and re["message"] =="success":
        print(f"{logistics_order_code},打印面单成功")
    else:
        print(f"{logistics_order_code},打印面单失败")


# 敦煌下单接口
def create_order_DHL(config):
    url = config + "/open-api/dhlink/order/asn"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
    "api_key": " INcNRb7gN3cOngaG",
    "api_username": "860031",
    "is_test": "false",
    "logistics_product_id": "817",
    "order_number": random.randint(1111111111,9999999999),
    "order_time": "2021-11-11T14:43:35+08:00",
    "paid_with_platform": "false",
    "parcel": {
        "declare_value": 10,
        "has_battery": "false",
        "has_flammable": "false",
        "has_liquid": "false",
        "has_metal": "false",
        "has_powder": "false",
        "height": 1,
        "length": 1,
        "price_currency": "usd",
        "price_unit": "dollar",
        "product_list": [
            {
                "declare_value": 2,
                "description_en": "test",
                "description_local": "测试",
                "has_battery": "false",
                "has_metal": "false",
                "height": 0,
                "hs_code": "88888",
                "is_flammable": "false",
                "is_liquid": "false",
                "is_powder": "false",
                "length": 0,
                "quantity": 5,
                "weight": 0.26,
                "width": 0
            },
            {
                "declare_value": 45,
                "description_en": "test1",
                "description_local": "测试",
                "has_battery": "false",
                "has_metal": "false",
                "height": 0,
                "hs_code": "88888",
                "is_flammable": "false",
                "is_liquid": "false",
                "is_powder": "false",
                "length": 0,
                "quantity": 5,
                "weight": 0.26,
                "width": 0
            }
        ],
        "quantity": 1,
        "weight": 1.3,
        "weight_unit": "kg",
        "width": 1
    },
    "payment_account": {
        "id": "109668"
    },
    "pickup": {
        "address_en": {},
        "address_local": {
            "city": "深圳市",
            "country": "中国",
            "name": "Emma zhu",
            "province": "广东省",
            "street_address1": "中国 广东省 深圳市 南山区 新百佳服装"
        },
        "phone": "6666"
    },
    "pickup_type": 1,
    "receiver": {
        "address_en": {
            "city": "Oyugis",
            "country": "Kenya",
            "name": "Quai Lin",
            "province": "Homa Bay County",
            "street_address1": "Oyugis Secondary School oyugis town",
            "street_address2": "Oyugis Secondary School oyugis town"
        },
        "address_local": {
            "city": "Oyugis",
            "country": "Kenya",
            "name": "Quai Lin",
            "province": "Homa Bay County",
            "street_address1": "Oyugis Secondary School oyugis town",
            "street_address2": "Oyugis Secondary School oyugis town"
        },
        "country_code": "KE",
        "email": "",
        "phone": "234-999900",
        "zipcode": "960609"
    },
    "require_label": "true",
    "return": {
        "address_en": {
            "city": "Beijing",
            "country": "China",
            "name": "jia",
            "province": "Beijing",
            "street_address1": "China Beijing Beijing dongchengqu Montgomery"
        },
        "address_local": {},
        "phone": "13567899875"
    },
    "sender": {
        "address_en": {
            "city": "Beijing",
            "country": "China",
            "name": "jia",
            "province": "Beijing",
            "street_address1": "China Beijing Beijing dongchengqu Montgomery"
        },
        "address_local": {},
        "country_code": "CN",
        "phone": "13567899875",
        "zipcode": "925301"
    },
    "timestamp": "2021-11-11T14:43:35+08:00",
    "tracking_number":  random.randint(1111111,9999999)   # 随机生成7位trackingId
}
    re = requests.post(url,headers=headers,json=payload,verify=False)
    # print(type(re.text))  # 返回值是json格式
    re = json.loads(re.text)
    print(re)
    # if re["message"] == "success":
    #     print(f"下单成功 ")
    #     print("订单号为：" + re["logistics_order_code"])
    #     print("tracking_id:" + re["tracking_id"])
    #     return re["logistics_order_code"], re["tracking_id"]  # 返回运单号和trackingId
    # else:
    #     print("下单失败")


if __name__ == "__main__":
    uat_config = "http://47.241.40.42:8480"
    # uat_config = "https://apis.speedaf.com/"  #如果切换生产环境，只需要传pro_config即可


    # 1-调用下单接口，拿到订单号和tracking_id
    info = create_order_wish(uat_config)
    logistics_order_code = info[0]
    tracking_id = info[1]

    # info = create_order_DHL(uat_config)
    # print(info)
    # 2-调用取消接口
    cancle_order(uat_config,tracking_id,logistics_order_code)

    # 3-拉取面单
    getFetchLabel(uat_config,tracking_id,logistics_order_code)