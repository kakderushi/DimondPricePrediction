# load the data
import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from sklearn.model_selection import train_test_split
from src.DimondPricePrediction.exception import customexception
from dataclasses import dataclass
from pathlib import Path
import sys
import os

class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemestone.csv")))  
            logging.info("i have dataset as a dataframe")
            
            # here i save my data into artifacts folder in raw data file
            os.makedirs(os.path.join(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have save the raw data in artifacts ")
            
            logging.info("train test split performed")
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split is completed")
            train_data.to_csv(self.ingestion_config.test_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part is completed")
            
        except Exception as e:
            logging.info
            ("exception during occured at data ingestion stage")
            raise customexception(e,sys)
            