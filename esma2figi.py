#!/usr/bin/env python3

import logging
import sys
from core import core


# main procedure
def main():

    logging.basicConfig(
        filename="esma2figi.log",
        format='%(asctime)s %(levelname)-8s %(filename)s %(lineno)d %(message)s  ',
        level=logging.ERROR,     # Possibilities: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    try:
        logging.debug("esma2figi.main() start")
        exit_status = core()

    except Exception as e:
        ex = str(e)
        logging.critical(f"Exception: {ex} ")
        exit_status = 0

    finally:
        
        logging.debug("esma2figi.main() end")   
        sys.exit(exit_status)


# Script start point
if __name__ == '__main__':
    main()
