import argparse
from datetime import date, datetime
import pefile


'''
Description: 
                        --> This script will get metadata from EXE file. 
To run this script      --> python metadata_pdf.py
example                 --> python metadata_pdf.py  blablabla.exe
'''


__authors__ = ["Gokan Bektas"]
__date__ = 20211215
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'A Tool to extract metadata from EXE files'

parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} on {}".format(", ".join(__authors__),__date__))
parser.add_argument("EXE_FILE", help="Path to exe file")
parser.add_argument("-v", "--verbose", help="Increase verbosity of output", action='store_true', default=False)
args = parser.parse_args()

pe = pefile.PE(args.EXE_FILE)

print(f"Decoding : {hex(pe.OPTIONAL_HEADER.Magic)}")

# in here we need to check if the executable has a 32-bit or 64-bit binary 
if hex(pe.OPTIONAL_HEADER.Magic) == '0x10b':
    print("This is a 32-bit binary")
    
if hex(pe.OPTIONAL_HEADER.Magic) == '0x20b':
    print("This is a 64-bit binary")
    
print(f"ImageBase: \t\t\t{hex(pe.OPTIONAL_HEADER.ImageBase)}")
print(f"SectionAlignment: \t\t{hex(pe.OPTIONAL_HEADER.SectionAlignment)}")
print(f"FileAlignment: \t\t\t{hex(pe.OPTIONAL_HEADER.FileAlignment)}")
print(f"SizeOfImage: \t\t\t{hex(pe.OPTIONAL_HEADER.SizeOfImage)}")
print(f"DllCharacteristics flags: \t{hex(pe.OPTIONAL_HEADER.DllCharacteristics)}")
print('DataDirectory: ')
print("-" * 50)

# next we need to print the name, size and virtual disk address of every DATA_ENTRY in DATA_DIRECORTY
for entry in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
    print(entry.name + "\n|---- Size : " + str(entry.Size) + "\n|---- VirtualAddress : " + hex(entry.VirtualAddress) +'\n')
print("-" * 50)