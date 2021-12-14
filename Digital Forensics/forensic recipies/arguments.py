#!/usr/bin/env python3

import argparse

'''
APACHE 2.0 LICENCE
'''

__authors__ = ["Gokan Bektas"]
__date__ = 20211213
__version__ = 1.0
__description__ = 'Basic Arguments'

"""
                        ########################## Educational Purpose !!! ##########################
# 
"""

parser = argparse.ArgumentParser(
    description=__description__,
    epilog='Developed by {}'.format(
        ", ".join(__authors__), __date__)    
)

parser.add_argument("INPUT_FILE", help="Path to input file")
parser.add_argument("OUTPUT_FILE", help="Path tp output  file")

parser.add_argument("--hash", help="Hash the files", action="store_true")

parser.add_argument("--hash-algorithm" ,help="Hash algorithm to use. ie md5, sha1, sha256", choices=['md5', 'sha1', 'sha256'], default="sha256")

parser.add_argument("-v", "--version", "--script-version",
                    help="Display script version information",
                    action="version", version=str(__version__)
                    )

parser.add_argument('-l', '--log', help="Path to log file", required=True)

args = parser.parse_args()

input_file = args.INPUT_FILE
output_file = args.OUTPUT_FILE

if args.hash:
    ha = args.hash_algorithm
    print("File hashing enabled with {} algorithm".format(ha))
if not args.log:
    print("Log file not defined. Will write to stdout")


'''
using the script:

python arguments.py Algorithms.txt rep.log --hash --hash-algorithm md5 -l log.txt

'''