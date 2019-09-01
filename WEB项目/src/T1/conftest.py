#！/usr/bin/python
#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import ui
from selenium.webdriver import ActionChains
import pytest
@pytest.fixture('module')
def dr():
    dr=webdriver.Chrome()
    dr.maximize_window()
    return dr