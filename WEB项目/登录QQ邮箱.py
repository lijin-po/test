#！/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get('https://mail.qq.com/cgi-bin/loginpage')
dr.maximize_window()
sleep(2)
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_class_name('switch_btn').click()
dr.find_element_by_id('u').send_keys('1778632232')
dr.find_element_by_id('p').send_keys('981007.li')
dr.find_element_by_id('login_button').click()
sleep(1)
dr.find_element_by_id('composebtn').click()

dr.switch_to.frame('mainFrame')
sleep(1)
dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('452286292@qq.com')
dr.find_element_by_id('subject').send_keys('web自动化')
dr.switch_to.frame(0) #dr.find_element_by_class_name('qmEditorIfrmEditArea')
dr.find_element_by_xpath('/html/body').send_keys('你好')
dr.switch_to.parent_frame()
dr.find_element_by_name('sendbtn').click()

sleep(2)
dr.quit()
