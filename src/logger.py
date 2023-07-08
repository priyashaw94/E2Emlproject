import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ##log file name format
logs_path=os.path.join(os.getcwd(), "logs",LOG_FILE)        ##setting path to current working dir
os.makedirs(logs_path,exist_ok=True)  ##keep on adding files even when the file exists

LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    with open(LOG_FILE_PATH) as f:
        logging.info("Logging has started...")