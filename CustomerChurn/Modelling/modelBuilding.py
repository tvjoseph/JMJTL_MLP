'''
JMJPFU
24-Jan-2020
This is the script for model building.
'''

import pandas as pd
from sklearn.model_selection import train_test_split

class ModelBuild():
    # THis is the class for various methods within the model building process
    def __init__(self,dataFrame,configfile):
        self.dataFrame = dataFrame
        self.config = configfile

    def dataCreation(self):
        # Getting the train_test split and label from the config file
        splitRatio = float(self.config.get('modelling','train_test_split'))
        label = self.config.get('modelling','label')
        # Converting the label to numeric data type
        self.dataFrame[label] = pd.to_numeric(self.dataFrame[label])
        # Defining the dependent and independent variables
        X = self.dataFrame.drop(label,axis=1)
        Y = self.dataFrame[label]
        X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size = splitRatio ,random_state = 123)

        return X_train,X_test,y_train,y_test






