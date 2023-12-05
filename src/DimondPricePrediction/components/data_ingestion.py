import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exceptions import customexception

from sklearn.model_selection import train_test_split



class DataIngestion:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info(" i have read dataset as df")
            
            logging.info("here i performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")
            
        except Exception as e:
            pass
    
 