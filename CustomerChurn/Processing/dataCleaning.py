'''
JMJPFU
24-Jan-2020
This is the script for various methods for data cleaning like outlier treatment, normalization etc
'''

import numpy as np
class DataCleaning():
    def __init__(self,array):
        print('Inside the data clearning class')
        self.array = array

    def outlierClipping(self,qt):
        # qt is a constant to find the quantile value
        # Defining the lower and upper limits which are prescribed standard deviations from the mean
        lowLimit = 0 + qt
        upLimit = 1 - qt
        # Clipping the values which are greater than the lower and upper limits
        self.array[self.array < np.quantile(self.array,lowLimit)] = np.quantile(self.array,lowLimit)
        self.array[self.array > np.quantile(self.array,upLimit)] = np.quantile(self.array,upLimit)
        return self.array


