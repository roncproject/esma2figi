import json 
import logging
from API import API
#from esma2figi import line

line = 0

# Remove, any comma's found, because CSV - TODO: Should be improved 
def kill_comma(s):
    logging.debug("process.kill_comma() start")
    t = s
    try:
        ret = s.replace(',', '')
    except Exception as e:
        ret = t
        logging.debug("process.kill_comma() exception")

    finally:
        return ret


# Call API, print ESMA values, print all OpenFigi lines received per ISIN
def process_row(rw):
    logging.debug("process.process_row() start")    

    fromdate = rw[0].strip()
    todate = rw[1].strip()
    isin = rw[2].strip()
    transactions = rw[3].strip()
    turnover = rw[4].strip()        
    line = 0

    try:
        api = API()                     # TODO: Maybe move this up
        sentence = api.handle_response(isin)
        for collection in sentence:
            # Original ESMA values including ISIN
            print(fromdate, ",", todate, ",", isin, ",", transactions, ",", turnover, ",", end="")
            line += 1

            if (sentence == "No identifier found."):    
                # This ISIN is unknown, so print "None", and exit loop
                print("None, None, None, None, None, None, None, None, None, None, None, None, ")
                raise Exception(sentence)
            else:        
                # Go through received data, and print each line
                for key, valuex in collection.items():
                    value_no_comma = kill_comma (str (valuex))
                    print (value_no_comma, ",", end="")
                print ("")
            
    except Exception as e:
        ex = str(e)
        logging.error(f"Exception: {ex} at line: {line}")

    logging.debug("process.process_row() end")    

