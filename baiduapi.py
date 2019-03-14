import requests
import ssl
import base64

def get_access_token(user_ak, user_sk):
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    token_payload = {
        "grant_type": "client_credentials",
        "client_id": user_ak,
        "client_secret": user_sk
    }
    token_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    r = requests.get(token_url, headers=token_headers, params=token_payload)
    content = r.json()
    return content["access_token"]

def ocr_solve(path, access_token, ocr_url):
    jpgtxt = base64.b64encode(open(path, "rb").read())

    ocr_payload = {'access_token': access_token}
    ocr_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    ocr_data = {"image": jpgtxt,
        "image_type": "BASE64",
        #"url": "",
        #"group_id": "Personal",
        #"user_id": "MagHSK"
    }

    ocr_request = requests.post(ocr_url, params=ocr_payload, headers=ocr_headers, data=ocr_data)
    ocr_content = ocr_request.json()
    result = ocr_content['words_result']
    ret = []
    for words in result:
        ret.append(words['words'])
    return ret
