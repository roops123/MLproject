import logging
from datetime import datetime
import os

#LOG_FILE=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_PATH=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_PATH,exist_ok=True)

logging.basicConfig(
    filemode=LOG_FILE,
    format="[%(asctime)s] -%(lineno)d -%(name)s -%(levelname)s %(message)s",
    level=logging.INFO
)