#!/bin/usr/env python3


import argparse
from datetime import datetime as dt
import os
import sys

'''
Description: 

This script will gather information of filesystem given file_path. 

To run this script. file name <os_dir_walk.py> pass <file_path>
example: to print out = python metadata_files.py ~/Desktop/Projects/scripts ### to write a file add '>' <dir_path> ##

'''

__authors__ = ["Gokan Bektas"]
__date__ = 20211214
__version__ = 1.0   # version can bealways change so make sure you update after make a change. it has to be in quation. 
__description__ = 'Gather filesystem metadata of provided file'

parser = argparse.ArgumentParser(description=__description__, epilog='Develop by {} on {}'.format(", ".join(__authors__), __date__))
parser.add_argument("FILE_PATH", help="Path to file to gather metadata for")
args = parser.parse_args()
file_path = args.FILE_PATH


#creating stat_info variables and print commands for us to see what change we would like to see. 
stat_info = os.stat(file_path)
if "linux" in sys.platform or "darwin" in sys.platform:
    print(f'Change time: {dt.fromtimestamp(stat_info.st_ctime)}')
    
elif "win" in sys.sys.platform:
    print(f'Creation time: {dt.fromtimestamp(stat_info.st_ctime)}')
    
else:
    print(f"[-] Unsupported platform {sys.platform} detected. Cannot interpret creation/change timestamp. ")
    
print(f'Modification time: {dt.fromtimestamp(stat_info.st_mtime)}')
print(f'Access time: {dt.fromtimestamp(stat_info.st_atime)}')

print(f'File mode: {stat_info.st_mode}')
print(f'File inode: {stat_info.st_ino}')

major = os.major(stat_info.st_dev)
minor = os.minor(stat_info.st_dev)

print(f'Device ID: {stat_info.st_dev}')
print(f'Major: {major}')
print(f'Minor: {minor}')

print(f'Number of hard links: {stat_info.st_nlink}')
print(f'Owner User ID: {stat_info.st_uid}')
print(f'Group ID: {stat_info.st_gid}')
print(f'File Size: {stat_info.st_size}')

print(f'Is a symlink: {os.path.islink(file_path)}')
print(f'Absolute path: {os.path.abspath(file_path)}')
print(f'File exists: {os.path.exists(file_path)}')
print(f'Parent directory: {os.path.dirname(file_path)}')
print("Parent directory: {} | File name: {}".format(*os.path.split(file_path)))