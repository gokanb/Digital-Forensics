import sys
import csv

def write_csv(data, output):
    if data == []:
        print('[-] No outpur results to write')
        sys.exit(4)
        
    print(f'[+] Writing output for {len(data)} domains with results to {output}')
    flatten_data = []
    field_list = ["URL", "Scan Date", "Servive", "Detected", "Result", "VirusToral Link"]
    for result in data:
        for service in result["Scans"]:
            flatten_data.append(
                {"URL": result.get("url", ""),
                 "Scan Date": result.get("scan_date", ""),
                 "VirusTotal Link": result.get("permalink", ""),
                 "Service": service,
                 "Detected": result["scans"][service]["detected"],
                 "Result": result["scans"][service]["result"]})
            
    with open (output, 'w', newlines='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_list)
        csv_writer.writeheader()
        for result in flatten_data:
            csv_writer.writerow(result)
        
