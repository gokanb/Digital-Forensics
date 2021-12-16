import sys
import csv

'''
creating csv writer so 
'''


def write_csv(data, output):
    if data == []:
        print('[-] No output results to write')
        sys.exit(4)
        
    print(f'[+] Writing output for {len(data)} domains with results to {output}')
    flatten_data = []
    field_list = ["URL", "Scan Date", "Service", "Detected", "Result", "VirusTotal Link"]
    for result in data:
        for service in result["scans"]:
            flatten_data.append(
                {"URL": result.get("url", ""),
                 "Scan Date": result.get("scan_date", ""),
                 "VirusTotal Link": result.get("permalink", ""),
                 "Service": service,
                 "Detected": result["scans"][service]["detected"],
                 "Result": result["scans"][service]["result"]})
            
    with open(output, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_list)
        csv_writer.writeheader()
        for result in flatten_data:
            csv_writer.writerow(result)