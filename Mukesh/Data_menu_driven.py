
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.linalg import eig
from sklearn.preprocessing import Imputer
from future_encoders import OrdinalEncoder,OneHotEncoder
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import sys
from numpy.linalg import eig


# In[25]:


try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle


# In[26]:


pickle_filename = "myAnalysis.pickle"
pd.set_option('display.max_columns', 20)


# In[2]:


from random import gauss
from random import seed
from pandas import Series
from pandas.tools.plotting import autocorrelation_plot
import statsmodels.api


# In[3]:


import tensorflow as tf
import keras
from keras.layers import Input,Dense
from keras.models import Model


# In[42]:


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
        # print('Performing missing value detection and handling on the numerical features: ')
        missing = self.num_df.columns[self.num_df.isna().any()].tolist()
        self.data_matrix = self.num_df.values
        if(len(missing)==0):
            print('The data does not contain any missing values')
            mis_flag = 0
        else:
            #print('The data contains missing values which should be handled')
            mis_flag = 1
            # print("")
            # print('The features with missing values: ')
            # for i in range(len(missing)):
            #     print(missing[i])
        if(mis_flag==1):
            if(strat_ch==1):
                imputer = Imputer(strategy = "mean")
            elif(strat_ch==2):
                imputer = Imputer(strategy = "median")
            elif(strat_ch==3):
                imputer = Imputer(strategy = "most_frequent")
            imputer.fit(self.data_matrix)
            self.data_matrix = imputer.transform(self.data_matrix)
            print("")
            print('The missing values have been detected and handled')
    
    def Scaling_decision(self,ch_num):
        if(ch_num==1):
            self.data_matrix = self.z_score_standardization(self.data_matrix)
            print('The data has been z-score standardized')
            # print('-------------------------------------------------------------------------------------')
        if(ch_num==2):
            self.data_matrix = self.max_min_normalization(self.data_matrix)
            print('The data has been max-min normalized')
            # print('-------------------------------------------------------------------------------------')
            
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


# In[43]:


a = Analysis('housing.csv')


# In[44]:


a.Entry()


# In[45]:


a.cat_to_num(1)


# In[46]:


a.MVD(1)


# In[47]:


a.Scaling_decision(1)


# In[48]:


a.Noise_detection()


# In[49]:


a.Multicollinearity_Analysis()


# In[50]:


a.Dim_Reduction(2,4)

