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
from Processing import DataProcessing

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

# Automated imputing using fancyimpute

autoImputed = dp.autImpute(dataFrame)

dataFrame = pd.DataFrame(autoImputed,columns=dataFrame.columns)
print('data Frame shape after Imputation',dataFrame.shape)
print(dataFrame.isnull().sum()*100/dataFrame.shape[0])









