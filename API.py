import json     
import requests     # 2.19.1
from key import OPENFIGI_KEY
import logging
import time
 
# Python class to nteract with OpenFIGI API 
# For info see: https://www.openfigi.com/api
class API:

    # Init class with various fields
    def __init__(self):
        logging.debug("API.__init__() start")

        self.openfigi_apikey = OPENFIGI_KEY  
        self.openfigi_url = "https://api.openfigi.com/v2/mapping"
        self.openfigi_headers = {"Content-Type": "text/json"}
        if self.openfigi_apikey:
            self.openfigi_headers["X-OPENFIGI-APIKEY"] = self.openfigi_apikey

        self.response_count = 0

        logging.debug("API.__init__() end")


    # Do the actual call
    def get_response(self, isin: str) -> str:
        logging.debug("API.get_response() start")

        json_obj = {}
        json_obj["idType"] = "ID_ISIN"
        json_obj["idValue"] = isin

        json_str = json.dumps(json_obj)
        json_lst = "[" + json_str + "]"

        try:
            response = requests.post(url=self.openfigi_url, headers=self.openfigi_headers, data=json_lst,  timeout=(60, 60))
        except Exception as e:
            ex = str(e)
            logging.error(f"Exception: {ex} at response: {self.response_count}")
            #logging.error(str(e))

        logging.debug("API.get_response() end")

        return response

    # Loop as long as no succesful response has been given by API
    # Check response, for config.problems, bad reply, etc. 
    # Pause or stop if needed, else return unpacked response  
    def handle_response(self, isin: str) -> str:
        logging.debug("API.handle_response() start")
        
        got_a_response = False
        got_an_exception = False
        got_a_problem = False
        sentence = None
        response = None

        while (got_a_response == False):

            sentence = None

            try:
                response = self.get_response(isin)        

            except Exception as e:
                ex = str(e)
                logging.critical(f"Exception: {ex} at response: {self.response_count}")
               
                got_an_exception = True
            else:
                if (response.status_code == 
                    200             # Status 200, so should be Ok
                ):
                    if (got_an_exception == True):
                        logging.warning("API.get_response() Exception dropped")
                        got_an_exception = False

                    if (got_a_problem == True):
                        logging.warning("API.get_response() Problem solved")
                        got_a_problem = False
                                                
                    got_a_response = True

                    result_dict = json.loads(response.text)   

                    # Unpack response
                    for results in result_dict:
                        for dat in results:
                            # Check response contains "data", and not "error" 
                            sentence = results[dat]
                            
                # Throw an error with any of these statuses
                elif (response.status_code in {          
                    400,            # Bad request.
                    401,            # Unauthorized. Apikey is invalid. 
                    404,            # Invalid url.	
                    405,            # Invalid HTTP method.
                    406,            # Unsupported 'Accept' type.
                    413,            # Payload too large. 
                    415             # Invalid Content-Type.                        
                }):        
                    raise Exception("API.get_response: Bad configuration")

                # Any of these statuses, take a pause
                elif (response.status_code in {         
                    429             # Too Many Requests. Reached rate limitations.	
                }):
                    time.sleep(60)  # TODO: A smarter solution for this  
                    got_a_problem = True
                elif (response.status_code in {      
                    500,            # Internal server error. Resend the request later.
                    503             # Service Unavailable.	
                }):
                    time.sleep(30)
                    got_a_problem = True
                # Dunno, so throw an error    
                else : 
                    raise Exception("API.get_response: Unknown response")

        logging.debug("API.handle_response() end")

        self.response_count += 1

        return  sentence 
