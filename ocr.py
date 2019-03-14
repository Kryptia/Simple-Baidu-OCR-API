import sys
import baiduapi

ak = "sKx14uTbbwylOgSOwBSD6Iux"
sk = "QyjkMi0Cz50cl865ROQpcInGhtzYtGve"
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

