#！/usr/bin/python
#-*-coding:utf-8-*-
import pytest
from time import sleep
@pytest.fixture()
def lr():
    url = "http://v.juhe.cn/cccn/to_telecodes.php"