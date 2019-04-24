#!/usr/bin/python3

import os
import threading
import time
from fsplit.filesplit import FileSplit

''' for encryption '''
import base64
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

stime = time.time()

''' creating 1 GB file '''
print("Creating 1 GB binary file . . .")
with open('ip_file', 'wb') as file:
   # use urandom with parameter in bytes
   size = 1 * 1024 * 1024 * 1024  # bytes
   file.write(os.urandom(size))

''' checking ip file size '''
print(os.stat('ip_file').st_size)
print("Done.")
    
''' splitting 1 GB into 1024 1 MB files '''
print("Splitting 1 GB binary file into 1 MB files . . .")
split_size = 1 * 1024 * 1024  # bytes
fs = FileSplit(file='ip_file', splitsize=split_size, output_dir='split_files')
fs.split()

n_chunks = int(float(size) / float(split_size) + 1)
print("Done.")

''' encryption using multi-threading (Fernet cryptography) '''
class myThread(threading.Thread):
   def __init__(self, threadID, file_name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.file_name = file_name

   def run(self):
      print ("Starting encrypting file: " + self.file_name)
      encrypt_file(self.file_name)
      print ("Done encrypting file: " + self.file_name)

def encrypt_file(file_name):
   input_file = "split_files/" + file_name
   output_file = "encrypted_files/" + file_name + "_enc"

   with open(input_file, 'rb') as f:
      data = f.read()

   fernet = Fernet(key)
   encrypted = fernet.encrypt(data)

   with open(output_file, 'wb') as f:
      f.write(encrypted)

no_of_file = n_chunks
thread_list = [ myThread(n+1, "ip_file_" + str(n+1)) for n in range(no_of_file)]

for n in range(no_of_file):
    thread_list[n].start()
for n in range(no_of_file):
    thread_list[n].join()
print("Done.")

''' Finally joining into one file '''
print("Merging encrypted file chunks into one . . .")
with open('op_file_enc', 'w') as outfile:
   for n in range(1025):
        with open("encrypted_files/ip_file_" + str(n+1) + "_enc") as infile:
            outfile.write(infile.read())

''' checking op file size '''
print(os.stat('op_file_enc').st_size)
print("Done.")

etime = time.time()
print("time taken: " + str(etime - stime) + " sec")