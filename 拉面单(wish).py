import requests
import json

url = "http://47.241.40.42:8480/open-api/wish/order/getFetchLabel"

payload = {
    "api_key": "B2QoiMnuzjP7KrvI",
      "tracking_id": "33333",
    "logistics_order_code": "47234208662413",
}

headers = {
  'Content-Type': 'application/json',
}

response = requests.post(url, headers=headers, json=payload)
import pprint
pprint.pprint(response.text)

