#!/bin/usr/env python3


#importing libraries to use allow us run this script proper. 
import argparse 
import csv
import hashlib
import json
import os
import requests
import sys
import time


# importing libraries we created such below:
from domain_query import query_domain 
from file_query import query_file
from csv_writer import write_csv 

'''
Description: 
                    --> This script will be using to review malicious website or files to analyze. We are going to use api key from "VirusTotal" website. 
                
                    
To run this script: --> python application.py <domain name / IPs > . "refers to save file same directory" /<directory name> <apikey>
example:            --> python application.py domains.txt ./results.csv key.txt
'''


__authors__ = ["Gokan Bektas"]
__date__ = '2021-12-16'
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'Tool to review malicious websites or files '



# create main function. 
def main(input_file, output, api, limit, type):
    objects = set()
    with open (input_file) as infile:
        for line in infile:
            if line.strip() != '':
                objects.add(line.strip())
                
     
               
    if type == 'domain':
        data = query_domain(objects, api, limit)
        
    else:
        data = query_file(objects, api, limit)
    write_csv(data, output)
    
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} on {}".format(', '.join(__authors__), __date__))
    parser.add_argument("INPUT_FILE", help="Text File containing list of file paths/hashes or domains/IPs ")
    parser.add_argument("OUTPUT_CSV", help='Output CSV with lookup results')
    parser.add_argument("API_KEY", help="Text File containing API key")
    parser.add_argument("-t", "--type", help="Tyepe of data: file or domain", choices=("file", "domain" ), default='domain')
    parser.add_argument('--limit', action='store_true', help="Limit request to comply with public API key restrictions")
    args = parser.parse_args()
    
    
    directory = os.path.dirname(args.OUTPUT_CSV)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
     
        
    if os.path.exists(args.INPUT_FILE) and os.path.isfile(args.INPUT_FILE):
        main(args.INPUT_FILE, args.OUTPUT_CSV, args.API_KEY, args.limit, args.type)
    
    else:
        print(f'[-] Supplied input file {args.INPUT_FILE} does not exist or is not a file')
        sys.exit(1)
                
               
                