import os
from urllib import response
import urllib
import json
import requests

while True:
    ip= input("What is your target IP?: ")
    url = "http://ip-api.com/json/"
    response = urllib.request.urlopen(url+ip)
    datas = response.read()
    values = json.loads(datas)

    print(f"IP: {values['query']}")
    print(f"City: {values['city']}")
    print(f"ISP: {values['isp']}")
    print(f"Country: {values['country']}")
    print(f"Time Zone: {values['timezone']}")

    break