import requests
import ssl

def get_access_token(app_ak, app_sk):
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    token_payload = {
        "grant_type": "client_credentials",
        "client_id": app_ak,
        "client_secret": app_sk
    }
    token_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    r = requests.get(token_url, headers=token_headers, params=token_payload)
    content = r.json()
    return content["access_token"]


