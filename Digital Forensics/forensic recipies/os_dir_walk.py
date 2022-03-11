#!/bin/usr/env python3

import argparse
import os

'''
Description: 

# This scripts aims to iterate over a directory and its subdirectories to recursively process all files.
# We will use this script list the directories path.

# To run this script. file name <os_dir_walk.py> pass <dir_path>
# example: python os_dir_walk.py ~/Desktop/Projects/scripts > directory_report.txt 

'''

__authors__ = ["Gokan Bektas"]
__date__ = 20211214
__version__ = 1.0   # version can bealways change so make sure you update after make a change. it has to be in quation. 
__description__ = 'OS Directory Walk'

# this section script will print out epilog. 
parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {} on {}".format(
        ", ".join(__authors__),__date__)
)

# this section script will ask for argument! require a path way. 
parser.add_argument("DIR_PATH", help="Path to directory")
args = parser.parse_args()
path_to_scan = args.DIR_PATH

#iterate over the path_to_scan 
for root, directories, files in os.walk(path_to_scan):
    #iterate ove the files in the current "root"
    for file_entry in files:
        #create the relative path to the file
        file_path = os.path.join(root, file_entry)
        print(file_path)
