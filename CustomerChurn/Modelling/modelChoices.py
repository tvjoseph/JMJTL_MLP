'''
JMJPFU
25-Feb-2020
This is the script for models
Lord bless this attempt of yours
'''
from sklearn.pipeline import Pipeline

class Modelling():
    def __init__(self,xtrain,xtest,ytrain,ytest,configfile):
        self.xtrain = xtrain
        self.xtest = xtest
        self.ytrain = ytrain
        self.ytest = ytest
        self.config = configfile
        print('train shape in Modelling class',self.xtrain.shape)
        print('test shape in Modelling class', self.xtest.shape)
        print('Y_train shape in Modelling class', self.ytrain.shape)

    def modelChoices(self):
        # Get the list of required models from the config file
        modellist = list( self.config.get('modelling', 'models').split(','))
        # Start an empty list for storing classifiers
        classifiers = []
        for model in modellist:
            if model == 'KNN':
                from sklearn.neighbors import KNeighborsClassifier
                classifiers.append(KNeighborsClassifier())
            elif model == 'RF':
                from sklearn.ensemble import RandomForestClassifier
                classifiers.append(RandomForestClassifier(random_state=123))
            elif model == 'Ada':
                from sklearn.ensemble import AdaBoostClassifier
                classifiers.append(AdaBoostClassifier(random_state=123))
            elif model == 'LR':
                from sklearn.linear_model import LogisticRegression
                classifiers.append(LogisticRegression(random_state=123))
        return classifiers

    def spotChecking(self):
        classifiers = self.modelChoices()
        modelScore = 0
        classSelect = 'NA'
        for classifier in classifiers:
            estimator = Pipeline(steps=[('classifier', classifier)])
            estimator.fit(self.xtrain, self.ytrain)
            mScore = estimator.score(self.xtest, self.ytest)
            print(classifier)
            print("model score: %.2f" % mScore)
            if mScore > modelScore:
                modelScore = mScore
                classSelect = classifier
        return modelScore,classSelect



