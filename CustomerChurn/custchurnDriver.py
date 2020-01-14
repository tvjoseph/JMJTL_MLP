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

id_cols = dp.featSep()
print(id_cols)


