'''
JMJPFU
13-Jan-2020
This is the file for data preprocessing
'''

# This scripts consolidates all the data preprocessing steps

import pandas as pd
import json

class DataProcessing:
    def __init__(self,configfile):
        print('Inside the DataProcessing class')
        self.config = configfile


    def dataReader(self):
        # The below line gets the file path from the configuration file
        filePath = self.config.get('DataFiles', 'dataFile')
        churn = pd.read_csv(filePath)
        return churn

    def featSep(self):
        churn = self.dataReader()
        # Getting the configuration as a list and then splitting on commas as the json method was giving error
        id_cols = list(self.config.get('featureEng', 'id_cols').split(','))

        return id_cols

