'''
JMJPFU
13-Jan-2020
This is the file for data preprocessing
'''

# This scripts consolidates all the data preprocessing steps

import pandas as pd

class DataProcessing:
    def __init__(self):
        print('Inside the DataProcessing class')


    def dataReader(self,configfile):
        # The below line gets the file path from the configuration file
        filePath = configfile.get('DataFiles', 'dataFile')
        churn = pd.read_csv(filePath)
        return churn

