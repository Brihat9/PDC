#!/usr/bin/python3
import base64
import threading
import time

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


exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, file_name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.file_name = file_name
   def run(self):
      print ("Starting " + self.file_name)
      encrypt_file(self.file_name)
      print ("Exiting " + self.file_name)

def encrypt_file(file_name):
   input_file = file_name
   output_file = file_name + "_enc"

   with open(input_file, 'rb') as f:
      data = f.read()

   fernet = Fernet(key)
   encrypted = fernet.encrypt(data)

   with open(output_file, 'wb') as f:
      f.write(encrypted)


# Create new threads
thread1 = myThread(1, "ip_file_1")
thread2 = myThread(2, "ip_file_2")

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")