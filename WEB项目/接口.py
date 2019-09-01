#！/usr/bin/python
#-*-coding:utf-8-*-
import requests
import pytest
from a import e

@pytest.mark.parametrize('x,y',e)
def test(x,y):
    url = "http://192.168.10.53:5000/login"
    payload = f"username={x}&password={y}"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "4b8a0f6c-e0e2-4747-8627-705ce5a0c057,7025b3b1-d75e-4948-bbf3-28330fff6def",
        'Host': "192.168.10.53:5000",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "26",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    try:
        assert 'welcome'in response.text
    except:
        assert 'login' in response.text