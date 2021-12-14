

import logging
import sys


'''
Description:  
                -->This script it helps me out as developer, warning me error and warning messages.
To run this script --> python log.py 
example --> python os_dir_walk.py ~/Desktop/Projects/scripts  to write on '>' <file_name.log>
'''

__authors__ = ["Gokan Bektas"]
__date__ = 20211214
__version__ = 1.0   # version can be always change so make sure you update after make a change. it has to be in quation. 
__description__ = 'This script it helps me out as developer, warning me error and warning messages. '

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

msg_fmt = logging.Formatter("%(asctime)-15s %(funcName)-20s" "%(levelname)-8s %(message)s")

strhndl = logging.StreamHandler(sys.stdout)
strhndl.setFormatter(fmt=msg_fmt)

fhndl = logging.FileHandler(__file__ + ".log", mode='a')
fhndl.setFormatter(fmt=msg_fmt)

logger.addHandler(strhndl)
logger.addHandler(fhndl)

logger.info("Information message")
logger.debug("debug message")

def function_one():
    logger.warning("warning message")

def function_two():
    logger.error("error message")

function_one()
function_two()