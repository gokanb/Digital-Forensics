

from collections import Counter
from html_output import output_html


def process_data(data, output_dir):
    html_table = ""
    for acq in data:
        html_table += f"<tr><td>{acq[0]}</td><td>{acq[1]}</td><td>{acq[2]}</td><td>{acq[3]}</td><td>{acq[4]}</td></tr>\n"
        
    
    device_types = Counter([x[2] for x in data])
    custodian_devices = Counter([x[1] for x in data])
    
    date_dict = {}
    for acq in data:
        date = acq[3].split(" ")[0]
        if date in date_dict:
            date_dict[date] += int(acq[4])
            
        else:
            date_dict[date] = int(acq[4])
    output_html(output_dir, len(data), html_table, device_types, custodian_devices, date_dict)