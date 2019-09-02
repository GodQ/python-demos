from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)

private_pem = rsa.exportKey()

with open('master-private.pem', 'w') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
    f.write(public_pem)

private_pem = rsa.exportKey()
with open('ghost-private.pem', 'w') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('ghost-public.pem', 'w') as f:
    f.write(public_pem)




message = 'hello ghost, this is a plian text'
with open('ghost-public.pem') as f:
     key = f.read()
     print 'public key:\n >>>>>%s<<<<'%key
     rsakey = RSA.importKey(key)
     cipher = Cipher_pkcs1_v1_5.new(rsakey)
     #print 'data_unb64:\n -----%s-----'%cipher.encrypt(message)
     cipher_text = base64.b64encode(cipher.encrypt(message))
     print cipher_text


with open('ghost-private.pem') as f:
     key = f.read()
     rsakey = RSA.importKey(key)
     cipher = Cipher_pkcs1_v1_5.new(rsakey)
     text = cipher.decrypt(base64.b64decode(cipher_text), None) #error return None
     print text



with open('master-private.pem') as f:
      key = f.read()
      rsakey = RSA.importKey(key)
      signer = Signature_pkcs1_v1_5.new(rsakey)
      digest = SHA.new()
      digest.update(message)
      sign = signer.sign(digest)
      signature = base64.b64encode(sign)
      print signature


with open('master-public.pem') as f:
     key = f.read()
     rsakey = RSA.importKey(key)
     verifier = Signature_pkcs1_v1_5.new(rsakey)
     digest = SHA.new()
     # Assumes the data is base64 encoded to begin with
     digest.update(message)
     is_verify = signer.verify(digest, base64.b64decode(signature))
     print is_verify


