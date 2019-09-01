#！/usr/bin/python
#-*-coding:utf-8-*-
from selenium import  webdriver
from time import  sleep
dr=webdriver.Chrome()
dr.maximize_window()
# dr.get('https://www.baidu.com/')
#
# dr.find_element_by_id('kw').send_keys('京东')
# sleep(2)
# dr.find_element_by_class_name('t').click()
# ww=dr.window_handles
# dr.switch_to.window(ww[-1])
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('cpu')
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
# dd=dr.find_element_by_xpath('//*[@id="J_selector"]/div[1]/div/div[2]/div[2]').find_elements_by_tag_name('li')
# for i in dd:
#     print(i.text)



dr.get('https://www.douban.com')
# 获取当前的窗口的句柄
ww=dr.current_window_handle
print(ww)
dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# 获取所有窗口的句柄
dd=dr.window_handles
print(dd)
# 切换窗口  根据句柄进行切换
dr.switch_to.window(dd[-1])
print(dr.title)
dr.find_element_by_xpath('//*[@id="db-nav-book"]/div[2]/div/ul/li[2]/a').click()
mm=dr.window_handles
print(mm)
dr.switch_to.window(mm[2])
print(dr.title)
dr.close()
sleep(3)
dr.switch_to.window(mm[1])
print(dr.title)