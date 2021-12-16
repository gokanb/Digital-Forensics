import sys
import os
import csv
import requests
import json
import time

from file_hash import hash_file

'''
    
'''

def query_file (files, api, limit):
    if not os.path.exists(api) and os.path.isfile(api):
        print(f'[-] API key file {api} does not exist or is not a file')
        sys.exit(3)
    
    
    with open(api) as infile:
        api = infile.read().strip()
    json_data = [] 
    
    print(f'[+] Hashing and Quering {len(files)} Files using VirusTotal API')
    count = 0
    for file_entry in files:
        if os.path.exists(file_entry):
            file_hash = hash_file(file_entry)
            
        elif len(file_entry) == 32:
            file_hash = file_entry
            
        else:
            continue
        count += 1
        params = {'resource': file_hash, 'apikey': api}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = response.json()
        if 'Scan finished' in json_response['verbose_msg']:
            json_data.append(json_response)
            
        if limit and count == 3:
            print('[!!] Halting execution for a minute to comply with public API key restrictions')
            time.sleep(60)
            print ('[!!] Contiuning execution of remaing files')
            count = 0 
            
    return json_data
            
    