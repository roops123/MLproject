import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Exported the student dataset in pandas dataframe')

            # Ensure the directory for train, test, and raw data paths exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train_test_split initiated:")


            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            logging.info("train_test_split done")
            logging.info("Storing training datatset to train.csv")
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logging.info("Storing testing dataset in test.csv")
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    DataTransformation_obj=DataTransformation()
    train_data,test_data,preobj=DataTransformation_obj.initiate_data_transformation(train_data,test_data)

            
    



