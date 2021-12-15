import argparse
from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime
import hashlib
import logging
import os
import ssl
import sys
from urllib.request import urlopen
import urllib.error


#script will scann domain and get links from website and gathering information and generating hash of each linf found and put into log file.
'''
Description: 
                    --> This script is used to identify and andextract all links from a web site gather data in steps:
                    * Accessing the site and identify all the initial links.
                    * Recursively find addional information and append it to a log.
                    * Generate a hash of each link found
                    
To run this script: --> python beatiful_soup_parser.py <domain> <-l> <dir<logs>
example:            --> python beatiful_soup_parser.py http://facebook.com -l facebook.log ./logs/
'''

__authors__ = ["Gokan Bektas"]
__date__ = '2021-12-15'
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'BeatifulSoup Website Preservation Tool'


logger = logging.getLogger(__name__)


def main (website, output_dir):
    base_name = website.replace('htpps://', '').replace('http://', '').replace('www.', '')
    link_queue = set()
    if "http://" not in website and "https://" not in website:
        logger.error(f'Exiting preservation - invalid user input: {website}')
        sys.exit(1)
    logger.info(f'Accesing {website} webpage')
    context = ssl._create_unverified_context()
    
    try:
        index = urlopen(website, context=context).read().decode('utf-8')
        
    except urllib.error.HTTPError as e:
        logger.error(f'Exiting preservation - unable to access page: {website}')
        sys.exit(2)
    
    logger.debug(f'Succesfully accessed {website}')
    write_output(website, index, output_dir)
    link_queue = find_links(base_name, index, link_queue)
    logger.info(f'Found {link_queue} initial links on webpage')
    recurse_pages(website, link_queue, context, output_dir)
    logger.info(f'Completed preservation of {website}')
    
        
def find_links(website, page, queue):
    for link in BeautifulSoup(page, 'html.parser', parse_only=SoupStrainer('a', href=True)):
        if website in link.get('href'):
            if not os.path.basename(link.get('href')).startswith('#'):
                queue.add(link.get('href'))
    return queue
    
    
def recurse_pages(website, queue, context, output_dir):
    processed = []
    counter = 0
    while True:
        counter +=1
        if len(processed) == len(queue):
            break
        
        for link in queue.copy():
            if link in processed:
                continue
            processed.append(link)
            
            try:
                page = urlopen(link,context=context).read().decode('utf-8')
                
            except urllib.error.HTTPError as e:
                msg = f'Error accesing webpage: {link}'
                logger.error(msg)
                continue
            write_output(link, page, output_dir, counter)
            queue = find_links(website, page , queue)
    logger.info(f'Identified {len(queue)} links throughout website')
    
    
def hash_data(data):
    sha512 = hashlib.sha512()
    sha512.update(data.encode('utf-8'))
    return sha512.hexdigest()


def hash_file(file):
    sha512 = hashlib.sha512()
    with open(file, 'rb') as in_file:
        sha512.update(in_file.read())
    return sha512.hexdigest()
    

def write_output(name, data, output_dir, counter=0):
    name = name.replace('http://', '').replace('https://', '').rstrip('//')
    directory = os.path.join(output_dir, os.path.dirname(name))
    if not os.path.exists(directory) and os.path.dirname(name) != '':
        os.makedirs(directory)
        
    logger.debug(f'Writing {name} to {output_dir}')
    logger.debug(f'Data Hash: {hash_data(data)}')
    path = os.path.join(output_dir, name)
    path = path + '-' +str(counter)
    with open(path, 'w') as outfile:
        outfile.write(data)
    logger.debug(f'Output File Hash: {hash_file(path)}')    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__, epilog="Developed by {} {}".format(", ".join(__authors__),__date__))
    parser.add_argument('DOMAIN', help='Website Domain')
    parser.add_argument("OUTPUT_DIR", help="Preservation Output Directory")
    parser.add_argument('-l', help="Log file path", default=__file__[:-3] + ".log")
    args = parser.parse_args()
    
    logger.setLevel(logging.DEBUG)
    msg_fmt = logging.Formatter("%(asctime)-15s" "%(levelname)-8s" "%(message)s")
    strhndl = logging.StreamHandler(sys.stderr)
    strhndl.setFormatter(fmt=msg_fmt)
    fhndl = logging.FileHandler(args.l, mode='a')
    fhndl.setFormatter(fmt=msg_fmt)
    
    logger.addHandler(strhndl)
    logger.addHandler(fhndl)
    
    logger.info('Starting Site Links Preservation')
    logger.debug(f'Supplied arguments: {sys.argv[1:]}')
    logger.debug(f'System {sys.platform}')
    logger.debug(f'Version {sys.version}')
    
    if not os.path.exists(args.OUTPUT_DIR):
        os.makedirs(args.OUTPUT_DIR)
        
    main(args.DOMAIN, args.OUTPUT_DIR)