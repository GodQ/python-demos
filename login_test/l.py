import requests
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

base_url = 'https://test2-ly.ehomepay.com.cn'
get_token_url = base_url + '/pre-escrow/rsa'
login_url = base_url + '/pre-escrow/login2.action'

username = '20220757'
password = '123456'

# Get cookies from the previous response set-cookie header
def get_cookie(r):
    cookies = dict()
    for cookie in r.headers['Set-Cookie'].split(';'):
        s = cookie.split('=')
        cookies[s[0]] = s[1] if len(s) == 2 else None
    return cookies

r = requests.post(get_token_url)
if r.status_code != 200:
    raise Exception("Can not get Token")

public_key = json.loads(r.content)['data']['public_key']
public_key = "-----BEGIN PUBLIC KEY-----\n%s\n-----END PUBLIC KEY-----" % public_key
print "Get public key:\n", public_key

rsakey = RSA.importKey(public_key)
cipher = PKCS1_v1_5.new(rsakey)
password_encrypted = base64.b64encode(cipher.encrypt(password))

form = {
    'username': username,
    'password': password_encrypted,
}
print "Request Form:\n", form

cookies = get_cookie(r)
r = requests.post(login_url, form, cookies=cookies)
print r.status_code, r.reason #, r.content
if r.status_code != 200:
    raise Exception("Can not login")

ret_url = json.loads(r.content)['data']['retUrl']
print ret_url

ret_url = base_url+ret_url
cookies = get_cookie(r)
headers = {'':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(ret_url, cookies=cookies)
print r.status_code, r.reason #, r.content

