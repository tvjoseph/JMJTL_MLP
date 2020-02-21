'''
JMJPFU
24-Jan-2020
This is the script for model building.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer

class ModelBuild():
    # THis is the class for various methods within the model building process
    def __init__(self,dataFrame,configfile):
        self.dataFrame = dataFrame
        self.config = configfile

    def datTransform(self,X):
        # This is the method to transform numerical and categorical data
        categorical_transformer = Pipeline(steps = [('onehot',OneHotEncoder(handle_unknown='ignore'))])
        # The below needs to be parametrised
        numeric_transformer = Pipeline(steps=[('scaler',StandardScaler())])
        numeric_features = X.select_dtypes(include=['int64','float64']).columns
        categorical_features = X.select_dtypes(include=['category']).columns
        preprocessor = ColumnTransformer(transformers=[('numeric',numeric_transformer,numeric_features),('Categorical',categorical_transformer,categorical_features)])
        X_tran = pd.DataFrame(preprocessor.fit_transform(X))
        return X_tran

    def dataCreation(self):
        # Getting the train_test split and label from the config file
        splitRatio = float(self.config.get('modelling','train_test_split'))
        label = self.config.get('modelling','label')
        # Converting the label to numeric data type
        self.dataFrame[label] = pd.to_numeric(self.dataFrame[label])
        # Defining the dependent and independent variables
        X = self.dataFrame.drop(label,axis=1)
        Y = self.dataFrame[label]
        # Doing the data transform on X by calling the dataTransform() function
        X = self.datTransform(X)
        # Generating the train and test sets
        X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size = splitRatio ,random_state = 123)

        return X_train,X_test,y_train,y_test








