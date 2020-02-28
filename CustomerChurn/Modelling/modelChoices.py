'''
JMJPFU
25-Feb-2020
This is the script for models
Lord bless this attempt of yours
'''
from sklearn.pipeline import Pipeline
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

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
        # Saving the final classifier
        savedPath = self.config.get('modelling', 'savePath')
        filename = savedPath + '/' + 'spotmodel.sav'
        pickle.dump(classSelect, open(filename, 'wb'))
        return modelScore,classSelect,filename

    def makeEstimator(self,param_grid,Classifier):
        pipe = Pipeline(steps=[('classifier', Classifier)])
        # Fitting the grid search
        estimator = GridSearchCV(pipe, cv=10, param_grid=param_grid)
        # Fitting on the training set
        estimator.fit(self.xtrain,self.ytrain)
        # Printing the
        print("Best: %f using %s" % (estimator.best_score_,estimator.best_params_))
        # Predicting with the best estimator
        pred = estimator.predict(self.xtest)
        # Getting the Classification report
        classReport = classification_report(pred,self.ytest)
        return pred,classReport



    # This is the function for fine tuning models

    def getModel(self):
        modelScore, Classifier,filename = self.spotChecking()
        # Getting the name of the model
        model_name = type(Classifier).__name__
        if model_name == 'RandomForestClassifier':
            print('Fine tuning Random forest classifier')
            param_grid = {"classifier__class_weight": ['balanced','balanced_subsample'],"classifier__n_estimators": [50, 100,200]}
            pred,classReport = self.makeEstimator(param_grid,Classifier)
            print(classReport)
            return pred,classReport
        elif model_name == 'LogisticRegression':
            print('Fine tuning Logistic Regression classifier')
            param_grid = {'classifier__penalty' : ['l1', 'l2'],'classifier__C' : [1,3, 5],'classifier__solver' : ['liblinear']}
            pred,classReport = self.makeEstimator(param_grid,Classifier)
            print(classReport)
            return pred,classReport








