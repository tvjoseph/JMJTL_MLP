'''
JMJPFU
This is only to experiment with different scripts
'''

'''
References
https://stackoverflow.com/questions/1773793/convert-configparser-items-to-dictionary
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
from ast import literal_eval

# Getting the details of the arguments
ap =argparse.ArgumentParser()
ap.add_argument('--configfile',required=True,help='This is the path to the configuration file')
args = ap.parse_args()

# Getting the paths of the system arguments
sys_arguments = sys.argv
default_cfg = ConfigParser()
# sys_arguments[2] is the path to the configuration file
default_cfg.read_dict(sys_arguments[2])
parS = default_cfg['fineTuning']['RFC']


print(type(parS))
print(parS)





'''
parS = {s:dict(default_cfg.items(s)) for s in default_cfg.sections()}
parS = literal_eval(default_cfg['fineTuning']['RFC'])
#print(parS{0})
print('RFC',parS)
print(type(parS))
pardic = default_cfg._sections
print(pardic)
print(type(pardic))
'''




'''

person_string = '{"classifier__n_estimators": [50, 100,200]}'
print(type(person_string))

person_dict = json.loads(person_string)
#json.loads()
par = json.dumps(person_dict, indent = 4, sort_keys=True)
print(par)
#print(par)
print(type(par))





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

import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))
'''