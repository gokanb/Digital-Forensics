import argparse

from dash import DASH
from table import TABLE
from demo import DEMO

from data_processing import process_data
from html_output import output_html


'''
Description: 
                    --> 
                
                    
To run this script: --> 
example:            --> 
'''


__authors__ = ["Gokan Bektas"]
__date__ = '2021-12-16'
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'Generates dashboard of sample acquisition information '

def main(output_dir):
    acquisition_data = (
        ["001", " Debbie Downer", "Mobile", "04/01/2017 15:10:28", "32"],
        ["002", " Elliot Mrk", "Mobile", "02/01/2002 114:25:25", "23"],
        ["003", " Jessica Awner", "Mobile", "09/06/2017 2:30:29", "240"],
        ["004", " Jonathan Armando", "Mobile", "09/06/2017 1:55:25", "59"],
        ["005", " Ricardo Lopez", "Mobile", "09/06/2017 13:45:41", "80"],
        ["006", " Mehmet Kara", "Mobile", "09/06/2017 18:43:52", "40"],
        ["007", " Ali Can", "Mobile", "09/06/2017 13:34:21", "18"]
    )
    
    print("[+] Processing acquisition data")
    process_data(acquisition_data, output_dir)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} on {}".format(", ".join(__authors__), __date__))
    parser.add_argument("OUTPUT_DIR", help="Desired Output Path")
    args = parser.parse_args()


    main(args.OUTPUT_DIR)
    
