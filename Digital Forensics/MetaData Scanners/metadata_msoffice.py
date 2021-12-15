import argparse
from datetime import datetime as dt
from xml.etree import ElementTree as etree
import zipfile

'''
Description: 
                    -->  
To run this script: --> 
example:            --> 
'''


__authors__ = ["Gokan Bektas"]
__date__ = 20211215
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'Acquiring metadata from Office files'

parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} on {}".format(", ".join(__authors__),
__date__))
parser.add_argument("Office_File", help="Path to office file to read")
args = parser.parse_args()

# Checking to see if we have a zip file as input
zipfile.is_zipfile(args.Office_File)

# Opening a MSOffice file (MS Offcie 2007 or later)
zfile= zipfile.ZipFile(args.Office_File)

# Extracting the key elements for processing
core_xml = etree.fromstring(zfile.read('docProps/core.xml'))
app_xml = etree.fromstring(zfile.read('docProps/app.xml'))
