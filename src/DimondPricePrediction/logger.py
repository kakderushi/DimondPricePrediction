
'''
Logging in Python refers to the practice of recording messages that provide
information about the status or behavior of a program during its execution. 
It's like taking notes about what your program is doing at different points in time, 
and it's immensely helpful for understanding and debugging your code.
'''
import logging
import os
from datetime import datetime
# name of the file
# strftime means string format time 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Here i join my file path to the current working dirctory folder which logs folder
Log_path=os.path.join(os.getcwd(),"logs")
# here i make directory(folder) logs
# estis_ok=True check the directory alreday created or not if it created it through an error
# to avoid this kind of error we used this (((extis_ok)))
os.makedirs(Log_path,exist_ok=True)
# here i join my folder path to the file path 
log_file_path=os.path.join(Log_path,LOG_FILE)
# here i 
logging.basicConfig(level=logging.INFO,filename=log_file_path,format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")