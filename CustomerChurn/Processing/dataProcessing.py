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
        date_cols = list(self.config.get('featureEng', 'date_cols').split(','))
        cat_cols = list(self.config.get('featureEng', 'cat_cols').split(','))
        return id_cols,date_cols,cat_cols
    def zeroImpute(self,dataFrame):
        zero_impute = list(self.config.get('imputeStg', 'zero_imp').split(','))
        # imputing the selected columns with zero where ever they are 'na'
        dataFrame[zero_impute] = dataFrame[zero_impute].apply(lambda x: x.fillna(0))
        return dataFrame,zero_impute
    def custImpute(self,dataFrame,cols,val):
        # Imputing custom values to the desired columns
        dataFrame[cols] = dataFrame[cols].apply(lambda x:x.fillna(val))
        return dataFrame
    def custDrop(self,dataFrame,val):
        # Identify columns which needs to be dropped based on the threshold values
        dropCols = list(dataFrame.apply(lambda col: True if col.isnull().sum()/dataFrame.shape[0] >= val else False))
        # Convert the list of columns into a data frame with indicators on which to drop
        colMap = pd.DataFrame({'features':dataFrame.columns,'drop':dropCols})
        # Get the list of those columns which needs to be dropped
        excCols = list(colMap.loc[colMap['drop'] == True]['features'])
        # Drop those columns from the data frame
        dataFrame = dataFrame.drop(excCols,axis = 1)
        return dataFrame,excCols

