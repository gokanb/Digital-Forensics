
import subprocess
import json


def query_domains(domains):
    json_data = []
    print(f'[+] Quering {len(domains)} domains/IPs using PassiveTotal API')
    for domain in domains:
        if "https://" in domain:
            domain = domain.replace("https://", "")
        elif "http://" in domain:
            domain = domain.replace("http://", "")
            
        process = subprocess.Popen(["pt-client", "pdns", "-q", domain], stdout=subprocess.PIPE)
        results, err = process.communicate()
        result_json = json.loads(results.decode())
        if 'message' in result_json:
            if 'quota_exceeded' in result_json['message']:
                print('[-] API Sear Quota Exceeded')
                continue
            
        result_count = result_json["totalRecords"]
        
        print(f'[+] {result_count} results for {domain}')
        if result_count == 0:
            pass
        
        else:
            json_data.append(result_json['results'])
            
    return json_data