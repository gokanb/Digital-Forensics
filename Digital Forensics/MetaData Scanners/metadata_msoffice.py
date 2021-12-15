import argparse
from datetime import datetime as dt
from xml.etree import ElementTree as etree
import zipfile

'''
Description: 
                    --> This script will get metadata 
To run this script: --> metadata_msoffic.py 
example:            --> metadata_msoffic.py <blablabla.docx> or 
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


# Core.xml tag mapping
core_mapping ={
    'title': 'Title',
    'subject': 'Subject',
    'creator': 'Creator',
    'keywords': 'Keywrods',
    'description': 'Description',
    'lastModifiedBy': 'Last Modified By',
    'modified': 'Modified',
    'created': 'Created',
    'category': 'Category',
    'contentStatus': 'Status',
    'revision': 'Revision'
}

for element in core_xml.getchildren():
    for key, title in core_mapping():
        if key in element.tag:
            if 'date' in title.lower():
                text = dt.strptime(element.text, "%y%m%d %H:%M:%S.f")
            else:
                text = element.text
            print(f'{title}: {text}')
            
app_mapping = {
    'TotalTime': 'Edit Time (minutes)',
    'Pages': 'Page Count',
    'Words': 'Words Count',
    'Characters': 'Character Count',
    'Lines' : 'Line Count',
    'Paragraphs': 'Paragraphs Count',
    'Company' : 'Company',
    'HyperlinkBase': 'HyperlinkBase',
    'Slides': 'Slide Count',
    'Notes': 'Note Count',
    'HiddenSlides': 'Hidden Slide Count'
}

for element in app_xml.getchildren():
    for key, title in app_mapping.items():
        if key in element.tag:
            if 'date' in title.lower():
                text = dt.strptime(element.text, "%y-%m-%dT%h:%M:%SZ")
            else:
                text = element.text
            print(f'{title}: {text}')

