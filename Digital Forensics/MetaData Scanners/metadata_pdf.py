#!/bin/usr/env python3

from argparse import ArgumentParser, FileType
import datetime
from PyPDF2 import PdfFileReader
import sys

'''
Description: 
                        --> This script will get metadata from pdf file. 
To run this script      --> python metadata_pdf.py
example                 --> python metadata_pdf.py  blablabla.pdf
'''
__authors__ = ["Gokan Bektas"]
__date__ = 20211215
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'Tool utility to extract metadata from PDF files'

parser = ArgumentParser(description=__description__, epilog="Develop by {} on {}".format(", ".join(__authors__),__date__))
parser.add_argument("PDF_FILE", help="File to extract metadata from", type=FileType('rb'))
args = parser.parse_args()

pdf_file = PdfFileReader(args.PDF_FILE)

xmpm = pdf_file.getXmpMetadata()
if xmpm is None:
    print("No XMP metadata found in document")
    sys.exit()
    
def custom_print(fmt_str, value):
    if isinstance(value, list):
        print(fmt_str.format(", ".join(value)))
        
    elif isinstance(value, dict):
        fmt_value = [":".join((k, v)) for k, v in value.items()]
        
    elif isinstance(value,str) or isinstance(value, bool):
        print(fmt_str.format(value))
        
    elif isinstance(value, bytes):
        print(fmt_str.format(value.decode()))
        
    elif isinstance(value, datetime.datetime):
        print(fmt_str.format(value.isoformat()))
        
    elif value is None:
        print(fmt_str.format("N/A"))
        
    else:
        print("warn: unhandled type {} found".format(type(value)))
        
custom_print('Title: ', xmpm.dc_title)
custom_print('Creator(s): ', xmpm.dc_creator)
custom_print('Contributors: ', xmpm.dc_contributor)
custom_print('Subject: ', xmpm.dc_subject)
custom_print('Description: ', xmpm.dc_description)
custom_print('Created: ', xmpm.xmp_createDate)
custom_print('Modified: ', xmpm.xmp_modifyDate)
custom_print('Event Dates: ', xmpm.dc_date)
custom_print('Created With: ', xmpm.xmp_creatorTool)
custom_print('Document ID: ', xmpm.xmpmm_documentID)
custom_print('Instance ID: ', xmpm.xmpmm_instanceID)
custom_print('Language: ', xmpm.dc_language)
custom_print('Publisher: ', xmpm.dc_publisher)
custom_print('Resource Type: ', xmpm.dc_format)
custom_print('Type: ', xmpm.dc_type)

if xmpm.custom_properties:
    print("Custom Properties: ")
    for key, value in xmpm.custom_properties.items():
        print("\t{}: {}".format(key, value))










