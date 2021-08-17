# -*- coding: utf-8 -*-
import requests


class OriLoginObj(object):

    def __init(self):
        self.url = "http://127.0.0.1:5000/doLogin"
        self.data = {"account": "freePHP", "password": "2323243"}

    def do_login_directly(self):
        res = requests.post(self.url, data=self.data)
        return res.text
