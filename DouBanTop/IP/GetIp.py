import copy

import requests


def Testproxy():
    return requests.get("http://192.168.3.88:8765?type=0&count=10").json()


def delet_proxy(proxy):
    return requests.get("http://192.168.3.88:8765/delete?ip={}".format(proxy))


def get_proxy():
    thisProxys = Testproxy()
    con = []
    i=0
    for thisProxy in thisProxys:
        proxies = {"http": "http://" + thisProxy[0] +":"+ str(thisProxy[1])}
        try:
            requests.get(url="http://icanhazip.com/", timeout=5, proxies=proxies)
            con.append(thisProxy)
        except Exception:
            print('不通过校验')
    return con


if __name__ == '__main__':
    print(get_proxy())
