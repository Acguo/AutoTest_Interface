# -*- coding: UTF-8 -*-
import requests
from pylog import Pylog

class HttpRequest:
    def __init__(self):
        self.session = requests.session()
        self.headers = {}
        self.txt = None

    def get(self,url,data=None):
        try:
            resp = self.session.get(url=url, params=data, headers=self.headers)
            return resp
        except Exception as e:
            Pylog.error(e)

    def post(self,url,data):
        try:
            resp = self.session.post(url=url, data=data, headers=self.headers)
            return resp
        except Exception as e:
            Pylog.error(e)

    def upload(self,url,files):
        try:
            resp = self.session.post(url=url, files=files)
            return resp
        except Exception as e:
            Pylog.error(e)

if __name__ == "__main__":
    pass