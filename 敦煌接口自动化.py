def test(data):
    timeline = str(int((time.time() + 0.5) * 1000))

    # data = {"waybillNoList": ["47234208648536"],"labelType": 2}

    myData = DesUtils.triple_des_encrypt(data, timeline)

    headers = {'content-type': 'application/json'}
    online = 'https://apis.speedaf.com/'
    url = f"http://47.241.40.42:8480/open-api/express/order/createOrder?appCode={appCode}&timestamp={timeline}"
    x = requests.post(url, data=myData, headers=headers)

    # print the response text (the content of the requested file):
    re = json.loads(x.text)

    if re['data'] != None:

        # aa = DesUtils.triple_des_decrypt(re['data'])
        print(DesUtils.triple_des_decrypt(re['data']))
    else:
        print(re)