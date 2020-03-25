'''
JMJPFU
13-Jan-2020
This is the library files for the customer churn use case.
Lord bless this attempt of yours
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import argparse
import sys
from configparser import ConfigParser
from Processing import DataProcessing , DataCleaning
from FeatureEng import FeProcess
from EDA import Plotting
from Modelling import ModelBuild,Modelling

print('Lord and my God bless this attempt of yours')

####################### Configuration details ###########################
# The below scripts are to define the configuration details

# Getting the details of the arguments
ap =argparse.ArgumentParser()
ap.add_argument('--configfile',required=True,help='This is the path to the configuration file')
args = ap.parse_args()

# Getting the paths of the system arguments
sys_arguments = sys.argv
default_cfg = ConfigParser()
# sys_arguments[2] is the path to the configuration file
default_cfg.read(sys_arguments[2])

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End of Configuration details $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

### Starting the input data processing step ##############

print('Start the input data processing steps')

dp = DataProcessing(default_cfg)
# Reading the data from the DataProcessing class
dataFrame = dp.dataReader()
# Getting the id columns date columns and category columns from the featSep() function
id_cols,date_cols,cat_cols = dp.featSep()
# Getting the numeric columns which are the columns other than the above
num_cols = [column for column in dataFrame.columns if column not in id_cols + date_cols + cat_cols]

# Getting all columns ending with nine
col_9_names = dataFrame.filter(regex='9$', axis=1).columns

## Imputing strategy #############
# In this step we define the type of imputing we have to do for different columns

# impute 1 : Getting back the columns where zero imputing have to be done
dataFrame,zero_impute = dp.zeroImpute(dataFrame)

## Dropping columns  ###########
# Here the dataframes are modified by dropping columns
print("Shape before dropping: ", dataFrame.shape)
dataFrame = dataFrame.drop(id_cols + date_cols,axis = 1)
print("Shape after dropping: ", dataFrame.shape)
## Impute missing values with -1 for categorical columns

# Get the custom impute value from the configuration file
custVal = default_cfg.get('imputeStg', 'custimpVal')
# Get the data frame after applying custom impute
dataFrame = dp.custImpute(dataFrame,cat_cols,custVal)

## Dropping columns with values more than certain threshold

# Getting the threshold value from the configuration file
threshVal = default_cfg.get('featureEng', 'threshVal')
# Getting the dataframe after dropping along with the list of the dropped columns
dataFrame,colMap = dp.custDrop(dataFrame,float(threshVal))
print('data Frame shape after dropping columns',dataFrame.shape)

# Automated imputing

autoImputed = dp.autImpute(dataFrame)

dataFrame = pd.DataFrame(autoImputed,columns=dataFrame.columns)
print('data Frame shape after Imputation',dataFrame.shape)



# Process based feature engineering

## Instantiating the Feature engineering process

## Implementing the first feature engineering process which is to filter and keep only high value customers
dataFrame = FeProcess(dataFrame).process1()
## Implementing the process2 which is to create target variable 'churn'
dataFrame = FeProcess(dataFrame).process2()
## Implementing the process3 which is to create new columns by subtracting 8th month with average of 6 & 7
dataFrame = FeProcess(dataFrame).process3()
print('Shape of data frame',dataFrame.shape)

## Updating category and numeric columns after removing the 9th month columns
cat_cols = [col for col in cat_cols if col not in col_9_names]
cat_cols.append('churn')
num_cols = [col for col in dataFrame.columns if col not in cat_cols]

print('Length of category columns',len(cat_cols))
print('Length of numeric columns',len(num_cols))

## Changing column type for the category and numeric columns
dataFrame[num_cols] = dataFrame[num_cols].apply(pd.to_numeric)
dataFrame[cat_cols] = dataFrame[cat_cols].apply(lambda column: column.astype("category"), axis=0)

## Exploratory data analysis

# Univariate plotting
Plotting().univariate(dataFrame.arpu_6)
# Bivariate plotting
Plotting().bivariate(dataFrame.churn,dataFrame.aon)

## Data Cleaning

# Outlier clipping on numerical columns

dataFrame[num_cols] = dataFrame[num_cols].apply(lambda array: DataCleaning(array).outlierClipping(0.03))

## Model building steps

X_train,X_test,y_train,y_test = ModelBuild(dataFrame,default_cfg).dataCreation()

# Spot checking with multiple models

print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

## Spot checking different models using pipelines

modelling = Modelling(X_train,X_test,y_train,y_test,default_cfg)

score,Classifier,filename = modelling.spotChecking()

print(score,Classifier)

# Getting the final model after fine tuning

pred,classReport = modelling.getModel()

print(classReport)

# Now to start a new branch to check out the anamaly detection


















