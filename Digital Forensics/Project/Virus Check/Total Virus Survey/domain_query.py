import sys
import os
import csv
import requests
import time
import json

def query_domain(domains, api, limit):
    if not os.path.exists(api) and os.path.isfile(api):
        print(f'[-] API key file {api} does not exist or is not a file')
        sys.exit(2)
        
    with open(api) as infile:
        api = infile.read().strip()
    json_data = []
    
    print(f'[+] Quering {len(domains)} Domains / IPs using VIrusTotal API')
    count = 0 
    for domain in domains:
        count += 1
        params = {'resource': domain, 'apikey': api, 'scan': 1}
        response = requests.post('https://www.virustotal.com/vtapi/v2/url/report', params=params)
        json_response = response.json()
        if 'Scan finished' in json_response['verbose_msg']:
            json_data.append(json_response)
            
        if limit and count == 3:
            print('[!!] Halting execution for a minute to comply wit hpublic API key restrictions')
            time.sleep(60)
            print('[!!] COntinuing execution of remaining Domains / IPs')
            count = 0 
            
    return json_data