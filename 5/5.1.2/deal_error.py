# -*- coding: utf-8 -*-
from urllib import request
from urllib.error import HTTPError

try:
    request.urlopen('https://www.soso.com')
except HTTPError as e:
    print(e.reason)
