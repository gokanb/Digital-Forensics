import os
import shutil

from size_calculator import calculate_size
from labels_return import return_labels
from series_returns import return_series
from dash import DASH
from table import TABLE
from demo import DEMO


def output_html(output, num_devices, table, devices, custodians, dates):
    print(f'[+] Rendering HTML and copy files to {output}')
    cwd = os.getcwd()
    bootstrap = os.path.join(cwd, 'light-bootstrap-dashboard')
    shutil.copytree(bootstrap, output)
    
    dashboard_output = os.path.join(output, 'dashboard.html')
    table_output = os.path.join(output, 'table.html')
    demo_output = os.path.join(output, 'assets', 'js', 'demo.js')
    
    with open(dashboard_output, 'w') as outfile:
        outfile.write(DASH.render(num_custodians=len(custodians.keys()), num_devices=num_devices, data=calculate_size(dates)))
        
    with open(table_output, 'w') as outfile:
        outfile.write(TABLE.render(table_body=table))
        
    with open(demo_output, 'w') as outfile:
        outfile.write(
            DEMO.render(bar_labels=return_labels(dates.keys()),
                        bar_series=return_series(dates.values()),
                        pi_labels=return_labels(devices.keys()),
                        pi_series=return_series(devices.keys()),
                        pi_2_labels=return_labels(custodians.keys()),
                        pi_2_series=return_series(custodians.values())))