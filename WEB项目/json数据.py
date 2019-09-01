#！/usr/bin/python
#-*-coding:utf-8-*-
"""
json：是一种轻量级的数据交互格式，JavaScript语言中的一种数据表现形式
python中没有json  json的格式和字典是一样的

json模块：用来解决python不识别json格式
"""
import json
import requests
a={"name":123,"age":12}
print(type(a))
# 将字典转换成json字符串
b=json.dumps(a)
print(type(b))
# 将json字符串转换为字典
c=json.loads(b)
print(type(c))

url=""
aa=requests.get(url)
# 以字节的方式接收结果   content
# 以字符串的方式接收结果  text
# 以json的方式接收结果   json
bb=aa.json()     #相当于json模块中json.loads()