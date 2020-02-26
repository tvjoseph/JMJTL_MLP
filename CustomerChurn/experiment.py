'''
JMJPFU
This is only to experiment with different scripts
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
from Modelling import ModelBuild
import pickle
import json

# Getting the details of the arguments
ap =argparse.ArgumentParser()
ap.add_argument('--configfile',required=True,help='This is the path to the configuration file')
args = ap.parse_args()

# Getting the paths of the system arguments
sys_arguments = sys.argv
default_cfg = ConfigParser()
# sys_arguments[2] is the path to the configuration file
default_cfg.read(sys_arguments[2])

par = default_cfg['fineTuning']['RFC']

print(par)
print(type(par))

'''
# load the model from disk
loaded_model = pickle.load(open('D:/JMJTL/JMJTL_MLP/CustomerChurn/Models/spotmodel.sav', 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

import ConfigParser
import json
IniRead = ConfigParser.ConfigParser()
IniRead.read('{0}\{1}'.format(config_path, 'config.ini'))
value = json.loads(IniRead.get('Section', 'Value'))

params = json.loads(r'par')
print(params)
print(type(params))
'''

