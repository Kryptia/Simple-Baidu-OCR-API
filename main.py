import json
import baiduapi
import sys
import ocr

with open("account.conf", "r") as f:
    dic = json.loads(f.read())
    ak = dic['ak']
    sk = dic['sk']

token = baiduapi.get_access_token(ak, sk)

if len(sys.argv) >= 1:
    jpgpath = sys.argv[1]
else:
    jpgpath = input("Please input a path: ")

result = ocr.solve(jpgpath, token, True)

with open("ocr_result.txt", "w") as f:
    for i in result:
        f.write(i + "\n")

for i in result:
    print(i)
