import sys
import baiduapi
import json
import base64
import requests

accurate_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
general_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

def solve(path, access_token, use_accurate=True):
    if use_accurate:
        ocr_url = accurate_url
    else:
        ocr_url = general_url

    jpgtxt = base64.b64encode(open(path, "rb").read())

    ocr_payload = {'access_token': access_token}
    ocr_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    ocr_data = {"image": jpgtxt,
        "image_type": "BASE64",
    }

    ocr_request = requests.post(ocr_url, params=ocr_payload, headers=ocr_headers, data=ocr_data)
    ocr_content = ocr_request.json()
    result = ocr_content['words_result']
    ret = []
    for words in result:
        ret.append(words['words'])
    return ret


