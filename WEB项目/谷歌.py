#！/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
# 访问网址
# dr.get('https://www.baidu.com/')
# 获取访问网址的标题
# print(dr.title)
# 获取访问的网址
# print(dr.current_url)
# 设置浏览器窗口的大小
# dr.set_window_size(width=400,height=800)
# 设置浏览器窗口最大化
dr.maximize_window()
# 设置浏览器窗口最小化
# dr.minimize_window()
# 设置浏览器的位置
# dr.set_window_position(400,400)
# sleep(2)
# dr.get('https://www.jd.com/')
# sleep(2)
# 回退到上一次页面
# dr.back()
# 前进到第二个页面
# sleep(2)
# dr.forward()

"""
核心：定位
1.id  2.class   3.name  4.link_text
5.tag_name   6.xpath  7.css   8.partial_link_text
id ，xpath，css，name   相对于其他的的来说更加准确
动作
1.click()
2.send_keys('内容')
"""
# 1.id定位
# dr.find_element_by_id('kw').send_keys('python')
# dr.find_element_by_id('su').click()
# 2.class_name(class属性的值)定位      唯一的
# dr.find_element_by_class_name('s_ipt').send_keys('python')

# 3.name定位  指的就是name属性的值
# dr.find_element_by_name('wd').send_keys('python')
# 4.link_text   文本定位   两个标签中间的
# dr.find_element_by_link_text('新闻').click()
# 5.partial_link_text  模糊文本
# dr.find_element_by_partial_link_text('加拿大驻香港').click()
# 6.tag_name  标签定位：通用来定位一组对象
# 7.xpath    路径标记语言：绝对路径  /、相对路径   //
# xml：可扩展性标记语言======内容跟HTML一样
# 作用：用来存储数据
# dr.find_element_by_xpath('//*[@id="u1"]/a[1]')
# 8.css
# dr.find_element_by_css_selector('#u1 > a:nth-child(1)').click()


# 定位一组元素：同时定位到多个元素，结果是个列表
"""
# 层级定位：先定位一个大范围，再从大范围中定位元素
#     先定位到父元素再定位到子元素加动作
dr.父元素.子元素.动作
父元素必须是唯一的
子元素可以是一组，可以是唯一的
"""
"""
dr.get('https://www.ctrip.com/')
ww=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
print(len(ww))
for i in ww:
    i.click()
    print(i.text)
    sleep(2)
dd=dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
for j in dd:
    j.click()
    print(j.text)
    sleep(2)
"""


# iframe：内嵌框架
"""
切换框架，只可以用ID的值，或name的值
没有ID和name，先定位到框架，在切换
ww=dr.find_element_by_xpath('//*[@id="login_frame"]')
dr.switch_to.frame(ww)
# 退出到上一层框架
dr.switch_to.parent_frame()
#退出到第一层页面
dr.switch_to.default_content()
切换框架，只能一层一层进入，退出可以直接退出到主框架


dr.get('https://qzone.qq.com/')
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_id('switcher_plogin').click()
dr.find_element_by_id('u').send_keys('1778632232')
dr.find_element_by_id('p').send_keys('981007.li')
dr.find_element_by_id('login_button').click()
"""

"""
浏览器管理窗口的原理
浏览器会对每个打开的窗口生成一个唯一标识窗口的句柄
谷歌产生的句柄是一堆字符串
火狐产生的是一堆数字
"""
# dr.get('https://www.douban.com')
# # 获取当前的窗口的句柄
# ww=dr.current_window_handle
# print(ww)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# # 获取所有窗口的句柄
# dd=dr.window_handles
# print(dd)
# # 切换窗口  根据句柄进行切换
# dr.switch_to.window(dd[-1])
# print(dr.title)


# 处理弹出框  alert弹出框
"""
dr.get('file:///C:/Users/pc/Desktop/abc.html')
dr.find_element_by_xpath('/html/body/button').click()
sleep(2)
# 处理弹出框  alert弹出框
# 将控制器切换到弹出框
a=dr.switch_to_alert()
print(a.text)  #获取弹出框上的文本
a.send_keys('ds') #给弹出框上输入内容
sleep(2)
# a.accept()  #点击弹出框上的确定
a.dismiss() #点击弹出框上的取消
"""


# dr.get('http://www.ifeng.com/')
# sleep(2)
#执行JavaScript函数
# 滚动条滚动到指定位置
# dd=dr.find_element_by_xpath('//*[@id="historyNewsList"]/div')
# sleep(1)
# dr.execute_script('arguments[0].scrollIntoView();',dd)

# ww=dr.find_element_by_xpath('//*[@id="financeNewsList"]/div')
# sleep(1)
# dr.execute_async_script('arguments[0].scrollIntoView();',ww)
# 2.更改页面的高度滑动滚动条，10000是高度
# for i in range(0,10000,200):
#     gd=f'var q=document.documentElement.scrollTop={i}'
#     dr.execute_script(gd)

# 智能等待
"""
from selenium.webdriver.support import ui
dr.get('https://www.jd.com')
sleep(2)  # 强制等待
# 智能等待
unti=ui.WebDriverWait(dr,20)
# 定位要出现的元素
unti.until(lambda dr:dr.find_element_by_xpath('//*[@id="navitems-group2"]/li[1]').is_displayed())
dr.find_element_by_xpath('//*[@id="navitems-group2"]/li[1]').click()
pp=dr.window_handles
"""


from selenium.webdriver.common.action_chains import ActionChains
# dr.get('https://www.jd.com/')
# ww=dr.find_elements_by_class_name('cate_menu_item')
# for i in ww:
#     # 动作链:动作链控制鼠标移动到某个元素的中心点
#     ActionChains(dr).move_to_element(i).perform()  #perform()  执行动作链
#     sleep(2)
# 拖拽
dr.get('https://qzone.qq.com/')
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_id('switcher_plogin').click()
dr.find_element_by_id('u').send_keys('92723432')
dr.find_element_by_id('p').send_keys('981043i23')
dr.find_element_by_id('login_button').click()
sleep(5)
dr.switch_to.frame('tcaptcha_iframe')
# dr.switch_to.frame(dr.find_element_by_xpath('//*[@id="tcaptcha_iframe"]'))
sleep(2)
fe=dr.find_element_by_id('tcaptcha_drag_button')   #拖拽的起始位置
# ActionChains(dr).drag_and_drop(1,2)         #拖拽   1.代表的拖拽的起始位置，2代表拖拽的结束位置
sleep(2)
ActionChains(dr).drag_and_drop_by_offset(fe,180,0).perform()   #将某个元素拖拽到某一点