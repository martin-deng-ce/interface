# -*- coding:utf-8 -*-
# @Time:2020/7/30 15:34
# @Author:martin
# @File:phone.py
import requests
# key = 63a77489d2c51d26b4031e344b4f0050
class Phone(object):

    def phone_location(self, phone, key):
        url = 'http://apis.juhe.cn/mobile/get'
        par = {
            "phone": phone,
            "key": key

        }
        r = requests.get(url=url,params=par)
        return r

if __name__ == '__main__':
    p = Phone()
    r = p.phone_location("13979296069","63a77489d2c51d26b4031e344b4f0050")
    print(r.text)