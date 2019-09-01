#！/usr/bin/python
#-*-coding:utf-8-*-
with open(r'D:\新建文件夹\WEB项目\until\a.txt','r') as f:
    m=f.read().split('\n')
print(m)
e=[]
for i in m:
   e.append(i.split(','))
print(e)