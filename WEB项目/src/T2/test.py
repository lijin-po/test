#！/usr/bin/python
#-*-coding:utf-8-*-
import requests
import pytest
from until.shuju import shuju,wu
from until.mylog import get_logger

log=get_logger(filename='test.py')
@pytest.mark.parametrize('x,y',shuju)
def test_1(x,y):
    url = "http://v.juhe.cn/cccn/to_telecodes.php"
    querystring = {"key":f"{x}","chars":f"{y}"}
    log.info(f'输入的参数为："key":f"{x}","chars":f"{y}"')
    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "b756ead2-0c78-44a3-8463-35bf56d6b02f,6b3ebdea-30b9-4e18-b205-261e04bd5d35",
        'Host': "v.juhe.cn",
        'Cookie': "aliyungf_tc=AQAAAPLgQHGeDAIA9rU3cyUP3rxyzqM5",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    # 使用的get请求方法    使用params 加参数值
    # 使用的post请求方法    使用data 加数据
    response = requests.request("GET", url, headers=headers, params=querystring)
    # response.status_code  #得到发送请求的状态码
    try:
        assert response.json()['reason'] == 'success'
    except:
        assert response.json()['result'] == None

# @pytest.mark.parametrize('x1,y1',wu)
# def test_2(x1,y1):
#     url = "http://v.juhe.cn/cccn/to_telecodes.php"
#     querystring = {"key":f"{x1}","chars":f"{y1}"}
#     log.info(f'输入的参数为："key":f"{x1}","chars":f"{y1}"')
#     headers = {
#         'User-Agent': "PostmanRuntime/7.15.2",
#         'Accept': "*/*",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "b756ead2-0c78-44a3-8463-35bf56d6b02f,6b3ebdea-30b9-4e18-b205-261e04bd5d35",
#         'Host': "v.juhe.cn",
#         'Cookie': "aliyungf_tc=AQAAAPLgQHGeDAIA9rU3cyUP3rxyzqM5",
#         'Accept-Encoding': "gzip, deflate",
#         'Connection': "keep-alive",
#         'cache-control': "no-cache"
#         }
#     # 使用的get请求方法    使用params 加参数值
#     # 使用的post请求方法    使用data 加数据
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     # response.status_code  #得到发送请求的状态码
#
#     assert response.json()['result'] == None
