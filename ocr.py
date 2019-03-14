import sys
import baiduapi
import json

with open("account.conf", "r") as f:
    dic = json.loads(f.read())
    ak = dic['ak']
    sk = dic['sk']

accurate_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
general_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

token = baiduapi.get_access_token(ak, sk)

if len(sys.argv) >= 1:
    jpgpath = sys.argv[1]
else:
    jpgpath = input("Please input a path: ")

url = accurate_url
result = baiduapi.ocr_solve(jpgpath, token, url)

for i in result:
    print(i)

