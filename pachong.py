import requests
page = 0
data = {
    "type": "suburb",
    "search": "",
    "page" : page
}
result = requests.post("http://index.buffaloex.com/express/searchPostcode", data=data)
result_list = result.json()["list"]
city_list = []
for i in result_list:
    city_list.append(i["text"])
print(city_list)

