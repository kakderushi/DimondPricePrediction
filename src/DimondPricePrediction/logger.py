import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(Log_path,exist_ok=True)
log_file_path=os.path.join(Log_path,LOG_FILE)
logging.basicConfig(level=logging.INFO,filename=log_file_path,format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")