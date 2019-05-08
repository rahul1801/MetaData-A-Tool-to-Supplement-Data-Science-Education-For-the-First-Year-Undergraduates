import numpy as np
import pandas as pd
import os
from numpy.linalg import eig
from sklearn.preprocessing import Imputer
from future_encoders import OrdinalEncoder, OneHotEncoder
from pandas.plotting import scatter_matrix

#import libraries for regression analysis
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import sys
from numpy.linalg import eig

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

pickle_filename = "myAnalysis.pickle"
pd.set_option('display.max_columns', 20)


from random import gauss
from random import seed
from pandas import Series
from pandas.tools.plotting import autocorrelation_plot
import statsmodels.api


import tensorflow as tf
import keras
from keras.layers import Input,Dense
from keras.models import Model


class Analysis:
    def __init__(self,url):
        url = str(url)
        self.data = pd.read_csv(url)
        print("Data Loaded.")
        self.cat_flag = 0
        self.num_flag = 0
        
    def Entry(self):
        op_count = 0
        flag = 0
        ans = 0
        ch_num = 0
        missing = []
        mis_flag = 0
        strat_ch = 0
        print('Data Type Summary: ')
        print("")
        print(self.data.info())
        print('-------------------------------------------------------------------------------------')
        print('An Introduction to the data')
        print("")
        print(self.data.head())
        cols = self.data.columns
        num_cols = self.data._get_numeric_data().columns
        cat_cols = list(set(cols) - set(num_cols))
        self.num_df = self.data[num_cols]
        self.cat_df = self.data[cat_cols]
        print('-------------------------------------------------------------------------------------')
        print('Identified numerical valued features: ')
        for i in range(self.num_df.shape[1]):
            print(self.num_df.columns[i])
            self.num_flag = 1
        print('-------------------------------------------------------------------------------------')
        print('Identified categorical valued features')
        for i in range(self.cat_df.shape[1]):
            print(self.cat_df.columns[i])
            self.cat_flag = 1
        print('-------------------------------------------------------------------------------------')
        self.data_frame = self.data
        unique = self.data_frame[self.data_frame.columns[self.data_frame.shape[1]-1]].unique().tolist()
        print(unique)
        print("")
        
        
    def z_score_standardization(self,data):
        for i in range(data.shape[1]):
                x = data[:,i]
                x_mean = np.mean(x)
                x_stdev = np.sqrt(np.mean(np.square(x)) - np.square(x_mean))
                z = (x - x_mean)/x_stdev
                data[:,i] = z
        return data

    def max_min_normalization(self,data):
        for j in range(data.shape[1]):
                x = data[:,j]
                x_min = min(x)
                x_max = max(x)
                x_maxmin = (x - x_min)/(x_max - x_min)
                data[:,j] = x_maxmin
        return data

    def Multicollinearity_Analysis(self):
        print('Performing Multicollinearity Analysis:')
        X = self.data_matrix[:,0:(self.data_matrix.shape[1]-1)]
        Y = self.data_matrix[:,(self.data_matrix.shape[1]-1)]
        graph_set = set([])
        corr_matrix = np.dot(X.T,X)/self.data_matrix.shape[0]
        print('Correlation Matrix Analysis:')
        print("")
        print(corr_matrix)
        print("")
        print('Correlation Analysis between Pair Wise Regressors: ')
        reg_count = 0
        print("")
        for i in range((corr_matrix.shape[0])):
            for j in range(i+1,corr_matrix.shape[1]):
                if(abs(corr_matrix[i][j])>0.9 and corr_matrix[i][j]<0.99):
                    print('Regressors: '+self.data_frame.columns[i]+' '+self.data_frame.columns[j])
                    graph_set.add(self.data_frame.columns[i])
                    graph_set.add(self.data_frame.columns[j])
                    reg_count+=1
        print("")
        print('-------------------------------------------------------------------------------------')
        print('Correlation Graphical Analysis: ')
        print("")
        graph_final = list(graph_set)
        if(reg_count>0):
            # scatter_matrix(self.data_frame[graph_final],figsize=(12,8))
            # plt.show()
            pass
        elif(reg_count==0):
            print('No multicollinearity detected between pair wise regressors')
            print("")

        e1,e2 = eig(corr_matrix)
        e1 = abs(e1)
        index = np.argsort(e1)[::-1]
        e2 = e2[:,index]
        condition_number = e1[0]/e1[(corr_matrix.shape[0]-1)]
        multicol=0
        if(condition_number>100):
            multicol=1
        else:
            multicol=0
        if(multicol==1):
            print('Multicollinearity exists in the data (eigen system analysis)')
        else:
            print('The data is free from any multicollinearity issue (eigen system analysis)')
        count=0
        if(multicol==1):
            for i in range(len(e1)):
                if(e1[0]/e1[i]>=100):
                    count+=1
            print('Result Post Eigen System Analysis:')
            print('Number of near linear dependencies in the data: '+str(count))
            corr_matrix_inv = np.linalg.inv(corr_matrix)
            vif_count=0
            print('VIF Values:')
            vif_max = 0
            vif_max_index = 0
            for i in range(len(corr_matrix_inv)):
                print(corr_matrix_inv[i][i])
                if(corr_matrix_inv[i][i]>vif_max):
                    vif_max = corr_matrix_inv[i][i]
                    vif_max_index = i
                if(corr_matrix_inv[i][i]>=10):
                    vif_count+=1  
            print("")
            print('Result Post VIF Analysis: ')
            print('Number of regressors exhibiting near linear dependence: '+str(vif_count))
            print('Feature exhibiting maximum multicollinearity: '+self.data_frame.columns[vif_max_index])
            
    def cat_to_num(self,ch):
        if(self.cat_flag==0):
            print('The data is devoid of any categorical features.')
            
        elif(self.cat_flag==1):
            if ch==1:      
                ordinal_encoder = OrdinalEncoder()
                df_encoded = ordinal_encoder.fit_transform(self.cat_df)
                print('The data has been ordinal/label encoded')
                return df_encoded
            elif ch==2:
                onehot_encoder = OneHotEncoder(sparse=False)
                df_1hot = onehot_encoder.fit_transform(self.cat_df)
                print('The data has been one-hot encoded')
                return df_1hot

    def MVD(self,strat_ch):
        missing = self.num_df.columns[self.num_df.isna().any()].tolist()
        self.data_matrix = self.num_df.values
        self.column_names = list(num_df.columns.values) #store column names

        if(len(missing)==0):
            print('The data does not contain any missing values')
            mis_flag = 0
        else:
            mis_flag = 1
        if(mis_flag==1):
            if(strat_ch==1):
                imputer = Imputer(strategy = "mean")
            elif(strat_ch==2):
                imputer = Imputer(strategy = "median")
            elif(strat_ch==3):
                imputer = Imputer(strategy = "most_frequent")
            imputer.fit(self.data_matrix)

            self.data_matrix = imputer.transform(self.data_matrix)
            #copy data_matrix to data_regres to feed into regression models
            self.data_regres = self.data_matrix
            #convert data_matrix to dataframe for visualisation
            self.data_visual = pd.DataFrame(data_matrix, columns=column_names)
            
            print("")
            print('The missing values have been detected and handled')
    
    def Scaling_decision(self,ch_num):
        if(ch_num==1):
            self.data_matrix = self.z_score_standardization(self.data_matrix)
            print('The data has been z-score standardized')
        if(ch_num==2):
            self.data_matrix = self.max_min_normalization(self.data_matrix)
            print('The data has been max-min normalized')
            
    def Noise_detection(self):
        noise = []
        cols = self.num_df.columns
        for i in range(len(cols)):
            k = 0
            series = Series(self.num_df[cols[i]])
            stats = statsmodels.stats.diagnostic.acorr_ljungbox(series, lags=None, boxpierce=False)
            vals = stats[1]
            if(vals.any()<=0.05):
                k = 1
            if(k==1):
                noise.append(cols[i])
        if(len(noise)==0):
            print('The features are devoid of White Gaussian and Gaussian Noise')
        else:
            print('The numerical features with Gaussian White Noise')
            print(noise)
    
    def PCA(self,data,f):
        X = self.data_matrix[:,0:(self.data_matrix.shape[1]-1)]
        cov_matrix = np.dot(X.T,X)/self.data_matrix.shape[0]
        e1,e2 = eig(cov_matrix)
        e1 = abs(e1)
        e2 = e2.T
        idx = np.argsort(e1)[::-1]
        e2 = e2[:,idx]
        e2 = e2[:,0:f]
        e1_sort = np.sort(e1)[::-1]
        self.data_matrix_reduced = np.matmul(X,e2)
        print(self.data_matrix_reduced.shape)
        sum1 = sum(e1_sort)
        sum_break = 0
        for i in range(f):
            sum_break+=e1_sort[i]
        retention = (sum_break/sum1)*100
        print('Percentage retention of features on applying PCA (linear transformation): '+str(retention))
        
    def Auto_Encoder(self,data,features):
        X = data[:,0:(data.shape[1]-1)]
        data_count = data.shape[0]
        f = features
        value = X.shape[1]
        input_value = Input(shape=(value,))
        hidden_value = int(0.80*(value))
        encoded_1 = Dense(hidden_value,activation='sigmoid')(input_value)
        encoded = Dense(f,activation='relu')(encoded_1)
        decoded_1 = Dense(hidden_value,activation='sigmoid')(encoded)
        decoded = Dense(value, activation='sigmoid')(decoded_1)
        autoencoder = Model(input_value,decoded)
        encoder = Model(input_value,encoded)
        autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
        autoencoder.fit(X,X,
                epochs=5,
                batch_size=int(data_count/5),
                shuffle=True)
        self.latent_representation = encoder.predict(X)
        print(self.latent_representation.shape)
        
    
    def Dim_Reduction(self,dim_ch,features):
        f = features
        if(dim_ch==1):
            self.PCA(self.data_matrix,f)
        elif(dim_ch==2):
            self.Auto_Encoder(self.data_matrix,features)
            
            

    def Linear_Regression_model(self,X, Y):
        xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size = 0.25, random_state = 0)
        LinearRegressor = LinearRegression()
        LinearRegressor.fit(xTrain, yTrain)
        yPrediction = LinearRegressor.predict(xTest)
        # Printing the results
        print('Results of Multivariate Regression')
        print('intercept            : \n', LinearRegressor.intercept_)
        print('Coefficients         : \n', LinearRegressor.coef_)
        print('Mean squared error   : %.2f' % mean_squared_error(yTest, yPrediction))
        print('Variance score       : %.2f' % r2_score(yTest, yPrediction))
        return yTest, yPrediction

    def Logistic_Regression_model(self, X, Y):
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)       
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        # Printing the results
        # Making the Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)

        print("Results of the Confusion Matrix")
        print("True Negatives: ",cm[0][0])
        print("False Postives: ",cm[0][1])
        print("False Negatives: ",cm[1][0])
        print("True Positives: ",cm[1][1])
        print("Results of Logistic Regression")
        print("Intercept value      : %.2f",classifier.intercept_)
        print("Mean Squared Error   : %.2f",mean_squared_error(y_test,y_pred))
        print("Coefficients         : %.2f",classifier.coef_)
        return y_test, y_pred

    def Exp_Regression_model(self, X, Y):
        X_exp = np.exp(X)
        xTrain, xTest, yTrain, yTest = train_test_split(X_exp, Y, test_size = 0.25, random_state = 0)
        LinearRegressor = LinearRegression()
        LinearRegressor.fit(xTrain, yTrain)
        yPrediction = LinearRegressor.predict(xTest)
        # Printing the results
        print('Results for Exponential Regression')
        print('intercept            : \n', LinearRegressor.intercept_)
        print('Coefficients         : \n', LinearRegressor.coef_)
        print('Mean squared error   : %.2f' % mean_squared_error(yTest, yPrediction))
        print('Variance score       : %.2f' % r2_score(yTest, yPrediction))
        return yTest, yPrediction

    def Regression_models(self, ch_reg):
        self.data_1 = self.data_regres #before scaling
        self.data_2 = self.data_matrix #after scaling

        X_1 = self.data_1[:,0:(self.data_1.shape[1]-1)]
        Y_1 = self.data_1[:,(self.data_1.shape[1]-1)]
        X_2 = self.data_2[:,0:(self.data_2.shape[1]-1)]
        Y_2 = self.data_2[:,(self.data_2.shape[1]-1)]

        if(ch_reg==1):
            #do multivariate / simple linear regression
            print("Analysis before data scaling")
            yt, y1 = self.Linear_Regression_model(X_1, Y_1)
            print("Analysis after complete data scaling")
            yt, y2 = self.Linear_Regression_model(X_2, Y_2)
            #plot graph
            plt.plot(yt, color='r') #actual y test value
            plt.plot(y1, color='g') #predicted y value before scaling
            plt.plot(y2, color='orange') #predicted y value after scaling
            plt.xlabel('Data set #')
            plt.ylabel('Target value')
            plt.show()
            plt.savefig('./images/LiR.png')

        elif(ch_reg==2):
            #do exponential regression
            print("Analysis before data scaling")
            yt, y1 = self.Exp_Regression_model(X_1, Y_1)
            print("Analysis after complete data scaling")
            yt, y2 = self.Exp_Regression_model(X_2, Y_2)
            #plot graph
            plt.plot(yt, color='r')
            plt.plot(y1, color='g')
            plt.plot(y2, color='orange')
            plt.xlabel('Data set #')
            plt.ylabel('Target value')
            plt.show()
            plt.savefig('./images/ExR.png')

        elif(ch_reg==3):
            #do logistic regression
            print("Analysis before data scaling")
            yt, y1 = self.Logistic_Regression_model(X_1, Y_1)
            print("Analysis after complete data scaling")
            yt, y2 = self.Logistic_Regression_model(X_2, Y_2)
            #plot graph
            plt.plot(yt, color='r')
            plt.plot(y1, color='g')
            plt.plot(y2, color='orange')
            plt.xlabel('Data set #')
            plt.ylabel('Target value')
            plt.show()
            plt.savefig('./images/LoR.png')

    def box_plot(features):
        fig = plt.figure(figsize=(20,8))
        
        df = data_visual[features]

        df.plot(kind="box")
        plt.ylabel("Number")

        my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
        my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
        my_file = '/images/box_plot.jpeg'       # Name of the scatter plot file
        fig.savefig(os.path.join(my_path, my_file))
        print("Saved Box plot")

    def hlines_plot(features): 
        fig = plt.figure(figsize=(20,8))
        x = list(data_visual[features[0]])
        x = np.unique(x)
        plt.hlines(1, np.min(x)-1, np.max(x)+1)
        plt.xlim(np.min(x)-1, np.max(x)+1)
        plt.ylim(0.5, 1.5)
        y = np.ones(np.shape(x))
        plt.plot(x, y, '|', ms = 40)
        xlabel = features[0]
        plt.title('HLines for '+ xlabel)

        my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
        my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
        my_file = '/images/hlines_plot.jpeg'       # Name of the scatter plot file
        fig.savefig(os.path.join(my_path, my_file))
        print("Saved HLines plot")

    def histogram_plot(features):
        xlabel = features[0]
        x = list(data_visual[features[0]])
        
        fig = plt.figure(figsize=(20,8))
        plt.hist(x,bins=20)
        plt.ylabel('No of times')
        plt.title(xlabel)

        my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
        my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
        my_file = '/images/histogram_plot.jpeg'       # Name of the scatter plot file
        fig.savefig(os.path.join(my_path, my_file))
        print("Saved Histogram plot")

    def scatter_plot(features):
        xlabel = features[0]
        ylabel = features[1]
        x = list(data_visual[features[0]])
        y = list(data_visual[features[1]])
        fig = plt.figure(figsize=(20,8))
        plt.scatter(x,y,alpha=0.5)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(xlabel+" vs "+ylabel)
        
        my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
        my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
        my_file = '/images/scatter_plot.jpeg'       # Name of the scatter plot file
        fig.savefig(os.path.join(my_path, my_file))
        print("Saved Scatter plot")

    def line_plot(features):
        xlabel = features[0]
        ylabel = features[1]
        x = list(data_visual[features[0]])
        y = list(data_visual[features[1]])
        fig = plt.figure(figsize=(20,8))
        
        plt.plot(x,y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(xlabel+" vs "+ylabel)

        my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
        my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
        my_file = '/images/line_plot.jpeg'       # Name of the scatter plot file
        fig.savefig(os.path.join(my_path, my_file))
        print("Saved Line plot")
        
def store_obj(filename,obj):
    pickle_file = open(filename,"wb")
    pickle.dump(obj,pickle_file)
    pickle_file.close()

def load_obj(filename):
    pickle_file = open(filename,"rb")
    obj = pickle.load(pickle_file)
    pickle_file.close()
    return obj

if __name__ == '__main__':
    arg = int(sys.argv[1])
    if arg == 0:
        myAnalysis = Analysis(sys.argv[2])
        store_obj(pickle_filename, myAnalysis)
    elif arg == 1:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Entry()
        store_obj(pickle_filename, myAnalysis)
    elif arg == 2:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.cat_to_num(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
    elif arg == 3:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.MVD(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
    elif arg == 4:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Scaling_decision(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
    elif arg == 5:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Multicollinearity_Analysis()
        store_obj(pickle_filename, myAnalysis)
    elif arg == 6:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Noise_detection()
        store_obj(pickle_filename, myAnalysis)
    elif arg == 7:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Dim_Reduction(int(sys.argv[2]), int(sys.argv[3]))
        store_obj(pickle_filename, myAnalysis)
    elif arg == 8:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Regression_models(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
    elif arg == 99:
        myAnalysis = load_obj(pickle_filename)
        print(len(myAnalysis.data.columns)-1)
        store_obj(pickle_filename, myAnalysis)