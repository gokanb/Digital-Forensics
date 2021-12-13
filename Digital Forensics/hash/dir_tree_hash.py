#!/bin/env python3

'''
# Author: Gokan Bektas
# Description:
                        ########################## Educational Purpose !!! ##########################
# this script will create a report. "from disk_hash adn import multi_hash" script will help us out encrypt 
# two different ways such as md5 and sha256. 
'''

from datetime import datetime
import os
from os.path import join, getsize
import sys
from disk_hash import multi_hash

def dir_report(base_path, reportfilename):
    """
    This will create a report containing file integrity information.
    base_path -- the directory with the files to index
    reportfilename -- the file to write the output to
    """
    with open(reportfilename, 'w') as out:
        out.write('File integrity information\n')
        out.write(f'Base path: {base_path}')
        out.write(f'Report created: {datetime.now().isoformat()}')
        out.write('"SHA-256,"MD5", "FileName", "FileSize"')
        out.write('\n')
        
    for root, dirs, files in os.walk(base_path):
        write_dir_stats(out, root, files)
    out.write('\n --- END OF REPORT')



def write_dir_stats(out, directory, files):
    """
    Writes status information on all specified files to the report 
    out -- open file handle of the report file
    directory-- the currently analyzed directory
    files -- list of files in that directory
    """
    
    for name in files:
        fullname = join(directory, name)
        hashes = multi_hash(fullname)
        size = getsize(fullname)
        out.write(f'{hashes[1]}, {hashes[0]}, {fullname}, {size}')
        out.write('\n')
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} reportFile baspath ')
        sys.exit(1)
    dir_report(sys.argv[2], sys.argv[1])
