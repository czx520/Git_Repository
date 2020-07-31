# -*- coding:utf-8 -*-
# @Time:2020/7/30 18:44
# @Author:whweia
# @File:login.py

import requests


class Byhy_Login():
    def __init__(self, s):
        self.s = s

    def login(self, user, pwd):
        url = 'http://127.0.0.1/api/mgr/signin'
        body = {
            'username':user,
            'password':pwd
        }
        r = self.s.post(url=url, data=body)
        return r


if __name__ == '__main__':
    s = requests.session()
    l = Byhy_Login(s)
    r = l.login('byhy', '88888888')
    print(r.text)
    print(type(r.json()['ret']))