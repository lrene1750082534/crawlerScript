#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = "http://60.205.1.103:30200/guttv/fdn/orderwatch"
id = "gzxmt_iptv|23010032020122121375933797"
# payload   ="['task_id' : '%s']" %id
payload = "[\r\n\t{\"task_id\": \"%s\"}\r\n]" % (id)
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
