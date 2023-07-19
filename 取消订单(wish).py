import requests
import json

url = "http://47.241.40.42:8480/open-api/wish/order/cancel"

payload = {
    "api_key": "B2QoiMnuzjP7KrvI",
    "tracking_id": "1908251",
    "logistics_order_code": "47234208649352",
    "cancel_reason": "input incorrect receiver addressfsaf",
    "carry_type": "2",
}

headers = {
  'Content-Type': 'application/json',
}

response = requests.post(url, headers=headers, json=payload)
import pprint
pprint.pprint(response.text)

