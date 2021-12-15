#!bin/usr/env python3


'''
# Author: Gokan Bektas
# Description:
                        ########################## Educational Purpose !!! ##########################
# This script will take file and encrypt md5 and sha256. 
to run this --> python disk_hash.py pass <filename> to encrypt
'''

import hashlib
import sys
from typing import Tuple

def multi_hash(filename):
    """
    This function will calculate the md5 and sha256 hashes
    of a specified file and return a list containing the has sums as hex strings.
    """
    
    md5 = hashlib.md5()
    sha256 = hashlib.sha512()
    
    with open(filename, 'rb') as f:
        
        while True:
            buf = f.read(2**20)
            if not buf:
                break
            
            
            md5.update(buf)
            sha256.update(buf)
            
    return [md5.hexdigest(), sha256.hexdigest()]


if __name__ == '__main__':
    hashes = []
    print('----------MD5 sums ----------')
    for filename in sys.argv[1:]:
        h = multi_hash(filename)
        hashes.append(h)
        
    print(f'{h[0]} {filename}')
    print('----------SHA@%^ sums ----------')
    for i in range(len(hashes)):
        print(f'{hashes[i][1]} {sys.argv[i+1]}')
        
        '''
        to use to script: python disk_hash.py pass <filename> to encrypt
        '''