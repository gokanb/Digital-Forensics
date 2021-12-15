import argparse
from datetime import date, datetime
from pefile import PE

'''
Description: 
                        --> This script will get metadata from EXE files. 
To run this script      --> python metadata_executable.py
example                 --> python metadata_executable.py  blablabla.exe
'''
__authors__ = ["Gokan Bektas"]
__date__ = 20211215
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'A Tool to extract metadata from EXE files'

parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} on {}".format(", ".join(__authors__),__date__))
parser.add_argument("-v", "--verbose", help="Increase verbosity of output", action='store_true', default=False)
args = parser.parse_args()

pe = PE(args.EXE_FILE)
ped = pe.dump_dict()

file_info = {}
for structure in pe.FileInfo:
    if structure.Key == b'StringFileInfo':
        for s_table in structure.StringTable:
            for key, value in s_table.entries.itens():
                if value is None or len(value) == 0:
                    value = "Unknown"
                file_info[key] = value
                
print("File Information")

for key, value in file_info.items():
    if isinstance(key,bytes):
        key = key.decode()
    if isinstance(value, bytes):
        value = value.decode()
    print(f'{key}: {value}')
    
#Defining  the compiling time
comp_time = ped['FILE_HEADER']['TimeDateStamp']['Value']
comp_time = comp_time.split("[")[-1].strip("]")
time_stamp, timezone = comp_time.rsplit(" ", 1)
comp_time = datetime.strptime(time_stamp, "%a %b %d %H:%M:%S %Y")
print("Compiled on {} {}".format(comp_time, timezone.strip()))

# Extract IOCs from PE Sections
print('\nSections: ')

for section in ped['PE Sections']:
    print("Section '{}' at {}: {}/{} {}".format(
        section['Name']['Value'], hex(section['VirtualAddress']['Value']),
        section['Misc_VirtualSize']['Value'],
        section['SizeOfRawData']['Value'], section['MD5'])
    )
    
# Display Imports, Names, and Adresses 
if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):          
    print("\nImports: ")
    for dir_entry in pe.DIRECTORY_ENTRY_IMPORT:
        dll = dir_entry.dll
        if not args.verbose:
            print(dll.decode(), end=", ")
            continue
        
        name_list = []
        for impts in dir_entry.imports:
            if getattr(impts, "name", b"Unknown") is None:
                name = b"Unknown"
            else:
                name = getattr(impts, "name", b"Unknown")
            name_list.append([name.decode(), hex(impts.address)])
        name_fmt = ["{} ({})".format(x[0], x[1]) for x in name_list]
        print('- {}: {}'.format(dll.decode(), ", ".join(name_fmt)))
    if not args.verbose:
        print()
        
# Display Exports, Names, and Adresses
if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
    print('\nExports: ')
    for sym in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print(f'-{sym.name.decode()}: {hex(sym.address)}')
    

