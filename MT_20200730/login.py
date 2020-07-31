# -*- coding:utf-8 -*-
# @Time:2020/7/30 18:46
# @Author:whweia
# @File:login.py

import requests


class MT_Login(object):
    def __init__(self, s):
        self.s = s
        self.host = 'http://192.168.232.129:8081'

    def login(self, user, pwd):
        url = self.host + '/recruit.students/login/in'
        par = {
            'account':user,
            'pwd':pwd
        }
        r = self.s.get(url=url, params=par)
        return r


if __name__ == '__main__':
    s = requests.session()
    l = MT_Login(s)
    r = l.login('admin1','660B8D2D5359FF6F94F8D3345698F88C')
    print(r.text)