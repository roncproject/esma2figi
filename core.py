import logging
import sys
import csv
from process import process_row


# Get input file name from commandline 
def get_arg():
    logging.debug("esma2figi.get_arg()")

    try:
        arg = sys.argv[1]

    except Exception as e:
        ex = str(e)
        logging.critical(f"Exception: {ex} ")

    logging.debug("esma2figi.get_arg() end")

    return arg


# Open input file
def core():   
    logging.debug("esma2figi.core() start")

    file_name = get_arg()
    read_csv(file_name)

    logging.debug("esma2figi.core() end")

    return 1


# Read input file 
def read_csv (fname):
    logging.debug("esma2figi.read_csv()")

    try:
        with open(fname) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                
                process_row (row)
    except Exception as e:
        ex = str(e)
        logging.critical(f"Exception: {ex} ")

    logging.debug("esma2figi.read_csv() end")

