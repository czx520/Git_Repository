# -*- coding:utf-8 -*-
# @Time:2020/7/30 18:52
# @Author:whweia
# @File:test_login_ddt.py

import ddt
import unittest
from MT_20200730.login import MT_Login
import requests

data = [
    {'user':'admin', 'pwd':'660B8D2D5359FF6F94F8D3345698F88C', 'expect':True},
    {'user':'admin1', 'pwd':'660B8D2D5359FF6F94F8D3345698F88C', 'expect':False},
    {'user':'', 'pwd':'660B8D2D5359FF6F94F8D3345698F88C', 'expect':False},
    {'user':'admin', 'pwd':'660B8D2D5359FF6F94F8D3345698F88C1', 'expect':False},
    {'user':'admin', 'pwd':'', 'expect':False}
]


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
