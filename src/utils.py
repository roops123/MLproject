import os
import sys
#import dill
import numpy as np
import pandas as pd
import pickle

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,pckl_obj):
    try:
        dir_name=os.path.dirname(file_path)

        os.makedirs(dir_name,exist_ok=True)

        with open(file_path,'wb') as file:
            pickle.dump(pckl_obj,file)
            logging.info(f"Object saved at {file_path}")

    except Exception as e:
        raise CustomException(e,sys)