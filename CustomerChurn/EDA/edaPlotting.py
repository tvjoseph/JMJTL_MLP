'''
JMJPFU
23rd Jan 2020
This script is for giving various methods for plotting
'''

import numpy as np
import seaborn as sns

class Plotting:
    # This class is for various methods of plotting

    def __init__(self):
        print('This is the plotting class')

    def vartypeCheck(self,variable):
        if variable.dtype == np.int64 or variable.dtype == np.float64:
            return 'numerical'
        elif variable.dtype == 'category':
            return 'categorical'
    def univariate(self,variable,stats=True):
        if self.vartypeCheck(variable) == 'numerical':
            sns.distplot(variable)
            if stats == True:
                print(variable.describe())

        elif self.vartypeCheck(variable) == 'categorical':
            sns.countplot(variable)
            if stats == True:
                print(variable.value_counts())
        else:
            print("Invalid variable passed: either pass a numeric variable or a categorical vairable.")

    def bivariate(self,var1,var2,stats=True):

        if self.vartypeCheck(var1) == 'numerical' and self.vartypeCheck(var2) == 'numerical':
            sns.regplot(var1, var2)
        elif (self.vartypeCheck(var1) == 'categorical' and self.vartypeCheck(var2) == 'numerical') or (
                self.vartypeCheck(var1) == 'numerical' and self.vartypeCheck(var2) == 'categorical'):
            sns.boxplot(var1, var2)

