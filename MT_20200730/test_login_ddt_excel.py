# -*- coding:utf-8 -*-
# @Time:2020/7/30 18:53
# @Author:whweia
# @File:test_login_ddt_excel.py

import ddt
import unittest
from MT_20200730.login import MT_Login
import requests
from MT_20200730.read_excel import ExcelUtil

fileName = 'testdata.xlsx'
sheetName = 'Sheet1'
d = ExcelUtil(fileName, sheetName)        # 实例化
data = d.dict_data()
print(data)


@ddt.ddt
class TestMTLogin(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.l = MT_Login(s)

    @ddt.data(*data)
    def test_MT_login(self, testdata):
        print(testdata)
        user = testdata['user']
        pwd = testdata['pwd']
        expect = testdata['expect']
        res = self.l.login(user, pwd)
        if '退出登录' in res.text:                 # 断言
            r = True
        else:
            r = False
        self.assertEqual(expect, r)


if __name__ == '__main__':
    unittest.main()