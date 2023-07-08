import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys): #fn for our own custom message for any error
# error_detail we retreive from sys module which has all the error info  
    _,_,exc_tb=error_detail.exc_info()   
    #exc_info gives 3 execution info, exc_tb nw stores the info where exception has occurred
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    

class CustomException(Exception):   ##this class inherits parent class Exception
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message



if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by 0 error...")
        raise CustomException(e,sys)