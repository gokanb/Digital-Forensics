import argparse
import csv
import json
import os
import subprocess
import sys

from domain_query import query_domains
from csv_writer import write_csv

'''
Description: 
                    --> This script will be tool to survey on IP address and domain. 
                
To run this script: --> 
example:            --> 
'''



__authors__ = ["Gokan Bektas"]
__date__ = '2021-12-16'
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = ' Tool to survey on IP addresses and domain'

def main(domain_file, output):
    domains = set()
    with open(domain_file) as infile:
        for line in infile:
            domains.add(line.strip())
    json_data = query_domains(domains)
    write_csv(json_data, output)
    
    
# def query_domains(domains):
#     json_data = []
#     print(f'[+] Quering {len(domains)} domains/IPs using PassiveTotal API')
#     for domain in domains:
#         if "https://" in domain:
#             domain = domain.replace("https://", "")
#         elif "http://" in domain:
#             domain = domain.replace("http://", "")
            
#         process = subprocess.Popen(["pt-client", "pdns", "-q", domain], stdout=subprocess.PIPE)
#         results, err = process.communicate()
#         result_json = json.loads(results.decode())
#         if 'message' in result_json:
#             if 'quota_exceeded' in result_json['message']:
#                 print('[-] API Sear Quota Exceeded')
#                 continue
            
#         result_count = result_json["totalRecords"]
        
#         print(f'[+] {result_count} results for {domain}')
#         if result_count == 0:
#             pass
        
#         else:
#             json_data.append(result_json['results'])
            
#     return json_data
    
    

# def write_csv(data, output):
#     if data == []:
#         print('[!!] No output results to write')
#         sys.exit(2)
        
#     print(f'[+] Writing output for {len(data)} domains/IPs with results to {output}')
#     field_list = ["value", "firstSeen", "lastSeen", "collected", "resolve", "resolveType", "source", "recordType", "recordHash"]
    
#     with open(output, 'w', newline='') as csvfile:
#         csv_writer = csv.DictWriter(csvfile, fieldnames=field_list)
#         csv_writer.writeheader()
#         for result in data:
#             for dictionary in result:
#                 csv_writer.writerow(dictionary)
    
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} on {}".format(", ".join(__authors__), __date__))
    parser.add_argument('INPUT_DOMAINS', help='Text File containing Domains and/or IPs')
    parser.add_argument("OUTPUT_CSV", help='Output CSV with lookup results')
    args = parser.parse_args
    
    directory = os.path.dirname(args.OUTPUT_CSV) #DOESNT WORK
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    if os.path.exists(args.INPUT_DOMAINS) and os.path.isfile(args.INPUT_DOMAINS):
        main(args.INPUT_DOMAINS, args.OUTPUT_CSV)
        
    else:
        print(f'[!!] Supplied input file {args.INPUT_DOMAINS} does not exists or is not a file')
        sys.exit(1)