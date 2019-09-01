#！/usr/bin/python
#-*-coding:utf-8-*-
with open(file=r'D:\新建文件夹\WEB项目\data\a.txt',mode='r',encoding='utf-8') as f:
    a=f.read().split('\n')
shuju=[]
for i in a:
    shuju.append(tuple(i.split(',')))
print(shuju)
with open(file=r'D:\新建文件夹\WEB项目\data\b.txt',mode='r',encoding='utf-8') as fb:
    b=fb.read().split('\n')
wu=[]
for j in b:
    wu.append(tuple(j.split(',')))
print(wu)
