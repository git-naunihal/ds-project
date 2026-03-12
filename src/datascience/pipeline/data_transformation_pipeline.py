from flask import config

from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from pathlib import Path

STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status=f.read().split(" ")[-1]
            
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data scheme is not valid")
        except Exception as e:
            print(e)
