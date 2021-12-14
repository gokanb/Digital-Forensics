#!/bin/usr/env python3

import logging
import multiprocessing as mp
from random import randint
import sys
import time

'''
Description:  
        -->This script will run multiprocess.
To run this script--> python multi_process.py
example --> 
'''
__authors__ = ["Gokan Bektas"]
__date__ = 20211214
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = ' multi procesesing script'

def sleeping(seconds):
    proc_name = mp.current_process().name
    logger.info(f'{proc_name} is sleeping for {seconds} seconds.')
    time.sleep(seconds)
    
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
msg_fmt = logging.Formatter("%(asctime)-15s %(funcName)-7s" "%(levelname)-8s %(message)s")
str_hndl = logging.StreamHandler(sys.stdout)
str_hndl.setFormatter(fmt=msg_fmt)
logger.addHandler(str_hndl)

num_workers = 10
workers = []
for i in range(num_workers):
    proc = mp.Process(target=sleeping, args=(randint(1, 20),))
    proc.start()
    workers.append(proc)
    
for worker in workers:
    worker.join()
    logger.info("Joined process {}".format(worker.name))
    
