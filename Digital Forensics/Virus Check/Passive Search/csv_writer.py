import sys
import csv

def write_csv(data, output):
    if data == []:
        print('[!!] No output results to write')
        sys.exit(2)
        
    print(f'[+] Writing output for {len(data)} domains/IPs with results to {output}')
    field_list = ["value", "firstSeen", "lastSeen", "collected", "resolve", "resolveType", "source", "recordType", "recordHash"]
    
    with open(output, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_list)
        csv_writer.writeheader()
        for result in data:
            for dictionary in result:
                csv_writer.writerow(dictionary)