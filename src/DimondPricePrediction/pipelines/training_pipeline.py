from src.DimondPricePrediction.components.data_ingestion import DataIngestion
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd
import numpy as np


obj=DataIngestion()
obj.initiate_data_ingestion