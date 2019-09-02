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

session = requests.Session()

print session.headers
r = session.post(get_token_url)
print r.headers
print session.headers
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

r = session.post(login_url, form)
print r.headers
#print r.status_code, r.reason, r.content
if r.status_code != 200:
    raise Exception("Can not login")

ret_url = json.loads(r.content)['data']['retUrl']
print ret_url

ret_url = base_url+ret_url
r = session.get(ret_url)
print r.status_code, r.reason #, r.content

