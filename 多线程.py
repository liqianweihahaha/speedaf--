"""
接口的压力测试demo
"""
import requests
import json
import threading
# from script import log_handler

# logger = log_handler.Logger('pressure_by_threading.log')


url = 'http://112.74.53.147:7071/app/order/batch-add'


def test_api():
    headers = {
        'Authorization': '',
        'AppVersion':'1.0.23',
        'Lang':'en_US'
    }
    try:
        response = requests.post(
            url=url,
            headers=headers,
            timeout=5)
        resp = json.loads(response.text)
        print(resp)
        if response.status_code == 200:
            print(resp)
        else:
            print(resp)
    except Exception as e:
        print('调用接口失败')


def run():
    threads_list = []
    # 创建线程
    for k, v in tokens.items():
        t = threading.Thread(target=test_api, args=(k, v))
        threads_list.append(t)

    # 开启线程
    for i in threads_list:
        i.start()
    for i in threads_list:
        i.join()


if __name__ == '__main__':
    run()
