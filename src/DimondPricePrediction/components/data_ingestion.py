#  To load the data  create class

import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exceptions import customexception

from sklearn.model_selection import  train_test_split
from datasclasses import dataclass
from pathlib import Path

class DataIngestion:
    def __init__(self):
       

    def initiate_data_ingestion(self):
        logging.info("data ingestion stated")

        try:
            pd.read_csv(F:\ineauron_course\ML_PROJECTS\Project\notebooks)
        except Exception as e:
            pass                