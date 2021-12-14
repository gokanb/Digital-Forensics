#!bin?usr/env python3

import argparse
import hashlib
import os

'''
MIT licence
'''
__authors__ = ["Gokan Bektas"]
__date__ = 20211213
__version__ = '1.1' #version always change so make sure the update. it has to be quation. 
__description__ = "A way to create a hash of file's name and contents."

'''
Description: 
----> This application will encrypt file and content. 
We will use the hash algorithms such as md5, sha1, sha256, sha512. those are all great algorithms. 

To run this script --> python file_hashing.py  <file_name> <hash_alg>
example: --> python file_hashing.py LICENCE.md md5

'''

available_algorithms = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512
}

parser = argparse.ArgumentParser(description=__description__, epilog='Develop by {} on {}'.format(", ".join(__authors__), __date__))
parser.add_argument("FILE_NAME", help="Path of file to hash")
parser.add_argument("ALGORITHM", help="Hash algorithm to use", choices=sorted(available_algorithms.keys()))
args = parser.parse_args()

input_file = args.FILE_NAME
hash_alg = args.ALGORITHM

file_name = available_algorithms[hash_alg]()
abs_path = os.path.abspath(input_file)
file_name.update(abs_path.encode())

print(f'The {hash_alg} of filename is: {file_name.hexdigest()}')

file_content = available_algorithms[hash_alg]()
with open(input_file, 'rb') as open_file:
    buff_size = 1024
    buff = open_file.read(buff_size)
    
    while buff:
        file_content.update(buff)
        buff = open_file.read(buff_size)
    
print(f"The {hash_alg} of the content is: {file_content.hexdigest()}")

