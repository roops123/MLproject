import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

'''
The idea of the DataTransformation class a modular code to transfrom data obtained from the data ingestion process. The data transformation process includes the follwing steps:
1.Identify the categorical and numerical columns in the datasets.
2.For the numerical columns:
    a. Handle missing values with SimpleImputer using the median strategy as mean is sensitive to outliers.
    b.Scale the data using StandardScaler.
3.For categorical columns:
    a.Handlle missing values with SimpleImputer using mode;most frequent value.
    b.Apply OnrHotEncoder to convert categorical values into numerical values.
    c.Scale the data using StandardScaler with paramter with_mean=false to avoid some feature having negative values.It scales the feature based on the variance of the data.
4.Use ColumnTransformer to apply the transformations to the respective columns.
5.

'''
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns=["reading_score",
                               "writing_score"]
            
            categorical_columns=["gender",
                                 "race_ethnicity",
                                 "parental_level_of_education",
                                 "lunch",""
                                 "test_preparation_course"]
            
            Numerical_pipeline=Pipeline(steps=[
                #Handling missing value using median strategy in SimpleImputer
                ("imputer",SimpleImputer(strategy="median")),
                #Scaling the data using StandardScaler
                ("scaler",StandardScaler())
            ])

            categorical_pipeline=Pipeline(steps=[
                #Handling missing value using mode strategy in SimpleImputer
                ("imputer",SimpleImputer(strategy="most_frequent")),
                #Performing OneHotEncoding to convert the categorical data into numerical data
                ("OneHotencode",OneHotEncoder()),
                #Scaling the data using StandardScaler with parameter with_mean=false to avoid some feature having negative values
                #It scales the feature based on the variance of the data.
                #This is done to avoid the data being skewed and to make the data more normal.
                ("scaler",StandardScaler(with_mean=False))
            ])

            logging.info(f"Numerical data:{numerical_columns}")
            logging.info(f"categorical data:{categorical_columns}")

            #Using ColumnTransformer to apply the transformations to the respective columns
            #The ColumnTransformer allows us to apply different transformations to different columns of the dataset.
            #The transformers parameter is a list of tuples where each tuple contains the name of the transformer, the transformer object, and the columns to which the transformer should be applied.
            preprocessor=ColumnTransformer(
                transformers=[
                    ("numerical_pipleine",Numerical_pipeline,numerical_columns),
                    ("Categorical_pipeline",categorical_pipeline,categorical_columns)
                ]
            )
            logging.info(f"Preprocessor object:{preprocessor}")
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            preprocessor_obj=self.get_data_transformer_object()

            #Loading train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info(f"Train data shape:{train_df.shape}")
            logging.info(f"Test data shape:{test_df.shape}")

            logging.info("Loaded train and test data successfully")
            target_column="math_score"

            logging.info(f"Target column:{target_column}")
            #Spiltting data into fetaures
            input_feature_df=train_df.drop(columns=[target_column],axis=1)
            target_feature_df=train_df[target_column]

            input_test_feature_df=test_df.drop(columns=[target_column],axis=1)
            target_test_feature_df=test_df[target_column]

            logging.info(f"Applying processing object on training dataframe and test dataframe")
            #Applying the preprocessor object on the training and test data

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_df)
            input_feature_test_arr=preprocessor_obj.transform(input_test_feature_df)

            train_array=np.concatenate((input_feature_train_arr,np.array(target_feature_df).reshape(-1, 1)),axis=1)
            test_array=np.concatenate((input_feature_test_arr,np.array(target_test_feature_df).reshape(-1, 1)),axis=1)

            logging.info("Preprocessing on training and test data completed")

            save_object(
                self.data_transformation_config.preprocessor_obj_file_path,
                preprocessor_obj
            )

            return(
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)

