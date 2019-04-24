import base64
import os

from cryptography.fernet import Fernet

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "password" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b"\xcb\xf9\x80\xa5\xd1\xc9e\xb4}\x02\xf5'\x87\x9a!\xe4" # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

''' encrypt '''
input_file = 'ip_file_1'
output_file = 'ip_file_1_enc'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)


''' decrypt '''

input_file = 'ip_file_1_enc'
output_file = 'ip_file_1_enc_dec'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

''' validate '''
f1=open("ip_file_1","rb")
f2=open("ip_file_1_enc_dec","rb")
for line1 in f1:
    for line2 in f2:
        if line1==line2:
            # print("SAME\n")
            pass
        else:
            print("validation error.")
        break
f1.close()
f2.close()
