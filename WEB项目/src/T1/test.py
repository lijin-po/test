#！/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import ui
from selenium.webdriver import ActionChains
from until.mylog import get_logger
log=get_logger('test.py')

def test(dr):
    log.info('输入网址')
    dr.get('https://mail.163.com/')
    assert dr.title=='163网易免费邮--中文邮箱第一品牌'
    log.info('成功登录网址')
def test_1(dr):
    sleep(2)
    dr.find_element_by_id('switchAccountLogin').click()
    log.info('单击账号密码登录')
    dr.switch_to.frame(dr.find_element_by_xpath('//*[@frameborder="0" and @scrolling="no"]'))
    dr.find_element_by_name('email').send_keys('13592386651')
    log.info('输入账号：13592386651')
    dr.find_element_by_name('password').send_keys('981007.li')
    log.info('输入密码：981007.li')
    dr.find_element_by_id('dologin').click()
    log.info('单击登录')
    print(dr.title)
    assert dr.title=='网易邮箱6.0版'
    log.info('登录成功')
def test_2(dr):
    sleep(2)
    dr.find_element_by_id("_mail_component_24_24").click()
    log.info('单击写信')
    dr.find_element_by_class_name('nui-editableAddr-ipt').send_keys('1778632232@qq.com')
    log.info('输入收件人')
    dr.find_element_by_xpath('//*[@class="nui-ipt-input" and @type="text" and @tabindex="1"]').send_keys('这是一封邮件')
    log.info('输入主题')
    dr.switch_to.frame(dr.find_element_by_class_name('APP-editor-iframe'))   #id   name    索引    先定位到他
    dr.find_element_by_class_name('nui-scroll').send_keys('你好')
    log.info('输入正文')
    dr.switch_to.parent_frame()
    dr.find_element_by_class_name('nui-toolbar-item').click()
    log.info('单击发送')
