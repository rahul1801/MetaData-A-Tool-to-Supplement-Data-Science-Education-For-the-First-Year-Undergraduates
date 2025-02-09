# -*- coding: utf-8 -*-
"""Data_menu_driven.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i8mpm3_oTZP4kyix-rOTBrsvzfHvlRhF
"""

from keras.layers import Input, Dense
import keras.backend as K
from keras.losses import mean_squared_error
from keras.models import Model
import keras
import tensorflow as tf
import statsmodels.api
from pandas.plotting import autocorrelation_plot
from pandas import Series
from random import seed
from random import gauss
import numpy as np
import pandas as pd
import seaborn as sns
import os
import io

from numpy.linalg import eig
from sklearn.preprocessing import Imputer
from future_encoders import OrdinalEncoder, OneHotEncoder
from pandas.plotting import scatter_matrix

# import libraries for regression analysis
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

pickle_filename = r"E:\IBM\Mukesh\myAnalysis.pickle"
pd.set_option('display.max_columns', 20)

counter_value = 0


class Analysis:

	# Helper Functions for Multi-Correlation Analysis
    def heatmap(self, x, y, **kwargs):
        if 'color' in kwargs:
            color = kwargs['color']
        else:
            color = [1]*len(x)

        if 'palette' in kwargs:
            palette = kwargs['palette']
            n_colors = len(palette)
        else:
            n_colors = 256  # Use 256 colors for the diverging color palette
            palette = sns.color_palette("Blues", n_colors)

        if 'color_range' in kwargs:
            color_min, color_max = kwargs['color_range']
        else:
            # Range of values that will be mapped to the palette, i.e. min and max possible correlation
            color_min, color_max = min(color), max(color)

        def value_to_color(val):
            if color_min == color_max:
                return palette[-1]
            else:
                # position of value in the input range, relative to the length of the input range
                val_position = float((val - color_min)) / (color_max - color_min)
                # bound the position betwen 0 and 1
                val_position = min(max(val_position, 0), 1)
                # target index in the color palette
                ind = int(val_position * (n_colors - 1))
                return palette[ind]

        if 'size' in kwargs:
            size = kwargs['size']
        else:
            size = [1]*len(x)

        if 'size_range' in kwargs:
            size_min, size_max = kwargs['size_range'][0], kwargs['size_range'][1]
        else:
            size_min, size_max = min(size), max(size)

        size_scale = kwargs.get('size_scale', 500)

        def value_to_size(val):
            if size_min == size_max:
                return 1 * size_scale
            else:
                # position of value in the input range, relative to the length of the input range
                val_position = (val - size_min) * 0.99 / \
                                (size_max - size_min) + 0.01
                # bound the position betwen 0 and 1
                val_position = min(max(val_position, 0), 1)
                return val_position * size_scale
        if 'x_order' in kwargs:
            x_names = [t for t in kwargs['x_order']]
        else:
            x_names = [t for t in sorted(set([v for v in x]))]
        x_to_num = {p[1]: p[0] for p in enumerate(x_names)}

        if 'y_order' in kwargs:
            y_names = [t for t in kwargs['y_order']]
        else:
            y_names = [t for t in sorted(set([v for v in y]))]
        y_to_num = {p[1]: p[0] for p in enumerate(y_names)}

        plot_grid = plt.GridSpec(
            1, 15, hspace=0.2, wspace=0.1)  # Setup a 1x10 grid
        # Use the left 14/15ths of the grid for the main plot
        ax = plt.subplot(plot_grid[:, :-1])

        marker = kwargs.get('marker', 's')

        kwargs_pass_on = {k: v for k, v in kwargs.items() if k not in [
                'color', 'palette', 'color_range', 'size', 'size_range', 'size_scale', 'marker', 'x_order', 'y_order'
        ]}

        ax.scatter(
            x=[x_to_num[v] for v in x],
            y=[y_to_num[v] for v in y],
            marker=marker,
            s=[value_to_size(v) for v in size],
            c=[value_to_color(v) for v in color],
            **kwargs_pass_on
        )
        ax.set_xticks([v for k, v in x_to_num.items()])
        ax.set_xticklabels([k for k in x_to_num], rotation=45,
                           horizontalalignment='right')
        ax.set_yticks([v for k, v in y_to_num.items()])
        ax.set_yticklabels([k for k in y_to_num])

        ax.grid(False, 'major')
        ax.grid(True, 'minor')
        ax.set_xticks([t + 0.5 for t in ax.get_xticks()], minor=True)
        ax.set_yticks([t + 0.5 for t in ax.get_yticks()], minor=True)

        ax.set_xlim([-0.5, max([v for v in x_to_num.values()]) + 0.5])
        ax.set_ylim([-0.5, max([v for v in y_to_num.values()]) + 0.5])
        ax.set_facecolor('#F1F1F1')

        # Add color legend on the right side of the plot
        if color_min < color_max:
            # Use the rightmost column of the plot
            ax = plt.subplot(plot_grid[:, -1])

            col_x = [0]*len(palette)  # Fixed x coordinate for the bars
            # y coordinates for each of the n_colors bars
            bar_y = np.linspace(color_min, color_max, n_colors)

            bar_height = bar_y[1] - bar_y[0]
            ax.barh(
                y=bar_y,
                width=[5]*len(palette),  # Make bars 5 units wide
                left=col_x,  # Make bars start at 0
                height=bar_height,
                color=palette,
                linewidth=0
            )
            # Bars are going from 0 to 5, so lets crop the plot somewhere in the middle
            ax.set_xlim(1, 2)
            ax.grid(False)  # Hide grid
            ax.set_facecolor('white')  # Make background white
            ax.set_xticks([])  # Remove horizontal ticks
            # Show vertical ticks for min, middle and max
            ax.set_yticks(np.linspace(min(bar_y), max(bar_y), 3))
            ax.yaxis.tick_right()  # Show vertical ticks on the right


    def corrplot(self, data, size_scale=500, marker='s'):
        # print(data)
        corr = pd.melt(data.reset_index(), id_vars='index')
        # print(corr)
        corr.columns = ['x', 'y', 'value']
        self.heatmap(
            corr['x'], corr['y'],
            color=corr['value'], color_range=[-1, 1],
            palette=sns.diverging_palette(20, 220, n=256),
            size=corr['value'].abs(), size_range=[0,1],
            marker=marker,
            x_order=data.columns,
            y_order=data.columns[::-1],
            size_scale=size_scale)
    
    def __init__(self, url, choice):
        url = str(url)
        self.target_detection = 0
        self.data = pd.read_csv(url)
        self.flag1 = 0
        if(choice==1):
          self.target_detection=1
        elif(choice==0):
          self.target_detection=0
        target_column = pd.DataFrame(
            self.data.iloc[:, (len(self.data.columns)-1)])
        val = target_column._get_numeric_data().columns
        if(len(val) != self.target_detection):
            self.flag1 = 1
            self.data = pd.DataFrame(
                self.data.iloc[:, 0:(len(self.data.columns)-1)])
            self.target_var = target_column
            print("")
        cols1 = self.data.columns
        num_cols1 = self.data._get_numeric_data().columns
        cat_cols1 = list(set(cols1) - set(num_cols1))
        num_pr = self.data[num_cols1]
        cat_pr = self.data[cat_cols1]
        if(choice == 1):                                # User says numerical target
            self.target_detection = 1
            frm = [cat_pr, num_pr]
        elif(choice == 0):                              # User says categorical target
            self.target_detection = 0
            frm = [num_pr, cat_pr]
        if(self.flag1 == 0):
            self.data_preview = pd.concat(frm, axis=1, sort=False)
        elif(self.flag1 == 1):
            pre = pd.concat(frm, axis=1, sort=False)
            frm2 = [pre, self.target_var]
            self.data_preview = pd.concat(frm2, axis=1, sort=False)
        self.col_preview = self.data_preview.columns
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
        # To save info as a csv
        buffer = io.StringIO()
        self.data.info(buf=buffer)
        info_as_string = buffer.getvalue()
        info_as_list = info_as_string.strip('\n').split('\n')[3:-2]
        for i in range(len(info_as_list)):
            temp_info = info_as_list[i].strip().split()
            if(len(temp_info)>4):
            	info_as_list[i] = temp_info[:-2] + temp_info[-1:]
            else:
            	info_as_list[i] = temp_info[:2] + temp_info[3:]
            if len(info_as_list[i])>3:
            	temp = []
            	temp.append(' '.join(info_as_list[i][:-2]))
            	temp.append(info_as_list[i][-2])
            	temp.append(info_as_list[i][-1])
            	info_as_list[i] = temp
        info_as_df = pd.DataFrame(data=info_as_list, columns=["Feature", "Non-null values", "Dtype"], index=np.arange(1, len(info_as_list)+1))
        info_as_df.to_csv('E:\\IBM\\Mukesh\\Entry_data\\info.csv',index=False)

        # To save head as a csv
        self.data.head().to_csv('E:\\IBM\\Mukesh\\Entry_data\\head.csv',index=False)

        cols = self.data.columns
        self.num_cols = self.data._get_numeric_data().columns
        self.cat_cols = list(set(cols) - set(self.num_cols))
        self.num_df = self.data[self.num_cols]
        self.cat_df = self.data[self.cat_cols]
   		
        # Numerical Features
        for i in range(self.num_df.shape[1]):
            if i < (self.num_df.shape[1]-1):
            	print(self.num_df.columns[i])
            else:
            	print(self.num_df.columns[i],end="")
            self.num_flag = 1
        
        # Delimiter
        print('!',end="")
        
        # Categorical Features
        for i in range(self.cat_df.shape[1]):
            if i < (self.cat_df.shape[1]-1):
            	print(self.cat_df.columns[i])
            else:
            	print(self.cat_df.columns[i],end="")
            self.cat_flag = 1
        
        # Delimiter
        print('!',end="")

        # Target Feature Nature
        tf_nature = ""
        if(self.target_detection == 1):
            tf_nature = 'Numerical'
        else:
            tf_nature = 'Categorical'
        self.data_frame = self.data
        if(self.flag1 == 0):
            print('Target Feature: ' +
                  self.data.columns[len(self.data.columns)-1]+' ('+tf_nature+')',end='')
            unique = self.data_frame[self.data_frame.columns[self.data_frame.shape[1]-1]
                                     ].unique().tolist()
        elif(self.flag1 == 1):
            print('Target Feature: '+self.target_var.columns[0]+' ('+tf_nature+')',end='')
            unique = self.target_var[self.target_var.columns[0]].unique(
            ).tolist()
        if(self.target_detection==0):
            print(' - '+str(len(unique))+' classes')
        else:
	        print("")

    def z_score_standardization(self, data):
        for i in range(data.shape[1]):
            x = data[:, i]
            x_mean = np.mean(x)
            x_stdev = np.sqrt(np.mean(np.square(x)) - np.square(x_mean))
            z = (x - x_mean)/x_stdev
            data[:, i] = z
        return data

    def max_min_normalization(self, data):
        for j in range(data.shape[1]):
            x = data[:, j]
            x_min = min(x)
            x_max = max(x)
            x_maxmin = (x - x_min)/(x_max - x_min)
            data[:, j] = x_maxmin
        return data

    def Multicollinearity_Analysis(self):
        X = self.data_matrix
        graph_set = set([])

        # Data Matrix as DF for Heatmap
        X_as_df = pd.DataFrame(data=X, columns=self.analysis_data.columns)

        # Correlation Matrix
        corr_matrix = np.dot(X.T, X)/self.data_matrix.shape[0]
        corr_matrix = np.around(corr_matrix,decimals=4)
        corr_as_df = pd.DataFrame(data=corr_matrix, columns=self.analysis_data.columns)
        corr_as_df.to_csv('E:\\IBM\\Mukesh\\Entry_data\\corr.csv',index=False)
        plt.figure(figsize=(8, 8))
        self.corrplot(X_as_df.corr())
        plt.savefig('corr_matrix.png',bbox_inches='tight',pad_inches = 0.2)

        # Strong Pair-Wise Correlation
        reg_count = 0
        pair_reg = []
        for i in range((corr_matrix.shape[0])):
            for j in range(i+1, corr_matrix.shape[1]):
                if(abs(corr_matrix[i][j]) > 0.9 and corr_matrix[i][j] < 0.99):
                    pair_reg_each = []
                    pair_reg_each.append(self.analysis_data.columns[i])
                    pair_reg_each.append(self.analysis_data.columns[j])
                    pair_reg_each.append(corr_matrix[i][j])
                    pair_reg.append(pair_reg_each[:])
                    graph_set.add(self.analysis_data.columns[i])
                    graph_set.add(self.analysis_data.columns[j])
                    reg_count += 1
        graph_final = list(graph_set)
        if(reg_count > 0):
            print("1!",end="")

            pair_reg_as_df = pd.DataFrame(data=pair_reg, columns=["Feature-1", "Feature-2","Value"])
            pair_reg_as_df.to_csv('E:\\IBM\\Mukesh\\Entry_data\\pair_reg.csv',index=False)
        
            scatter_matrix(self.data_frame[graph_final],figsize=(12,8))
            plt.savefig('scatter_matrix.png',bbox_inches='tight',pad_inches = 0.2)
        elif(reg_count == 0):
            # No pair-wise correlation
            print("0!",end="")

        e1, e2 = eig(corr_matrix)
        e1 = abs(e1)
        index = np.argsort(e1)[::-1]
        e2 = e2[:, index]
        condition_number = e1[0]/e1[(corr_matrix.shape[0]-1)]
        multicol = 0
        if(condition_number > 100):
            self.multicol = 1
        else:
            self.multicol = 0
        if(self.multicol == 1):
            # Multicollinearity exists
            print("1!",end="")
        else:
            # Multicollinearity doesn't exist
            print("0!",end="")
        count = 0
        # Result Post Eigen System Analysis
        cond_indices = []
        if(self.multicol == 1):
            for i in range(len(e1)):
                cond_indices.append(e1[0]/e1[i])
                if((e1[0]/e1[i]) >= 100):
                    count += 1
            cond_indices = np.around(cond_indices,decimals=4)
            # Number of near linear dependencies in the data
            # print("Near linear dependencies:"+str(count),end="!")
            corr_matrix_inv = np.linalg.inv(corr_matrix)
            vif_count = 0

            # VIF Values
            vif_values = []
            vif_max = 0
            vif_max_index = 0
            for i in range(len(corr_matrix_inv)):
                vif_values.append(corr_matrix_inv[i][i])
                if(corr_matrix_inv[i][i] > vif_max):
                    vif_max = corr_matrix_inv[i][i]
                    vif_max_index = i
                if(corr_matrix_inv[i][i] >= 10):
                    vif_count += 1
            vif_values = np.around(vif_values,decimals=4)
            # Number of regressors exhibiting near linear dependence
            # print(str(vif_count),end="!")
            # Feature exhibiting maximum Variance Inflation Factor
            # print(self.analysis_data.columns[vif_max_index])

            # Combine cond indices and vif values and write into a csv
            combined = []
            for i in range(len(vif_values)):
                comb_temp = []
                comb_temp.append(self.analysis_data.columns[i])
                comb_temp.append(cond_indices[i])
                comb_temp.append(vif_values[i])
                combined.append(comb_temp[:])
            combined_as_df = pd.DataFrame(data=combined, columns=["Feature", "Condition Index","VIF Value"])
            combined_as_df.to_csv('E:\\IBM\\Mukesh\\Entry_data\\combined.csv',index=False)

    def cat_to_num(self, ch):
        if(self.cat_flag == 0):
            self.df_encoded = pd.DataFrame()
            print('The data is devoid of any categorical features.')

        elif(self.cat_flag == 1):
            if ch == 1:
                ordinal_encoder = OrdinalEncoder()
                self.df_encoded = ordinal_encoder.fit_transform(self.cat_df)
                self.df_encoded = pd.DataFrame(self.df_encoded)
                self.df_encoded.columns = self.cat_cols
                print('The data has been ordinal/label encoded')
        self.Data_concatenation()
#             #to be handled later (post discussion)
#             elif ch==2:
#                 onehot_encoder = OneHotEncoder(sparse=False)
#                 df_1hot = onehot_encoder.fit_transform(self.cat_df)
#                 print('The data has been one-hot encoded')
#                 return df_1hot

    def Data_concatenation(self):
        if(self.cat_flag == 0):
            self.merged_data = pd.DataFrame(self.num_df)
        elif(self.num_flag == 0):
            self.merged_data = pd.DataFrame(self.df_encoded)
        else:
            self.num_df.reset_index(drop=True, inplace=True)
            self.df_encoded.reset_index(drop=True, inplace=True)
            if(self.target_detection == 0):
                data_frames = [self.num_df, self.df_encoded]
                self.merged_data = pd.concat(data_frames, axis=1, sort=False)
            elif(self.target_detection == 1):
                data_frames = [self.df_encoded, self.num_df]
                self.merged_data = pd.concat(data_frames, axis=1, sort=False)
        if(self.flag1 == 0):
            self.analysis_data = pd.DataFrame(
                self.merged_data.iloc[:, 0:(len(self.merged_data.columns)-1)])
            self.target_data = pd.DataFrame(
                self.merged_data.iloc[:, (len(self.merged_data.columns)-1)])
        elif(self.flag1 == 1):
            self.analysis_data = self.merged_data
            self.target_data = self.target_var

    def MVD(self, strat_ch):
        missing = self.analysis_data.columns[self.analysis_data.isna(
        ).any()].tolist()
        self.data_matrix = self.analysis_data.values
        length = len(self.data_matrix) - len(self.df_encoded)
        self.column_names = list(
            self.analysis_data.columns.values)  # store column names
        if(len(missing) == 0):
            print('The data does not contain any missing values')
            mis_flag = 0
        else:
            mis_flag = 1
        if(mis_flag == 1):
            if(strat_ch == 1):
                imputer = Imputer(strategy="mean")
            elif(strat_ch == 2):
                imputer = Imputer(strategy="median")
            elif(strat_ch == 3):
                imputer = Imputer(strategy="most_frequent")
            imputer.fit(self.data_matrix)
            self.data_matrix = imputer.transform(self.data_matrix)
            print("")
            print('The missing values have been detected and handled')
        # copy data_matrix to data_regres to feed into regression models
        if(self.target_detection==0 and self.num_flag==1):
            self.data_vis = pd.DataFrame(self.data_matrix[:,0:(self.num_df.shape[1])])
            self.data_vis.columns = self.num_df.columns
            con = [self.data_vis,self.target_data]
            self.data_vis = pd.concat(con,axis=1,sort=False)
        elif(self.target_detection==1 and (self.analysis_data.shape[1]==self.df_encoded.shape[1])):
          self.data_vis = pd.DataFrame()
          print('No numerical features present for data visualization.')
        elif(self.target_detection==1 and (self.analysis_data.shape[1]!=self.df_encoded.shape[1])):
            self.data_vis = pd.DataFrame(self.data_matrix[:,(self.df_encoded.shape[1]):(self.analysis_data.shape[1])])
            self.data_vis.columns = self.num_df.columns[0:(self.num_df.shape[1]-1)]
            con = [self.data_vis,self.target_data]
            self.data_vis = pd.concat(con,axis=1,sort=False)
        elif(self.target_detection==0 and self.num_flag==0):
          self.data_vis = pd.DataFrame()
          print('No numerical features present for data visualization.') 
        data_new = pd.DataFrame(self.data_matrix)
        data_new.reset_index(drop=True, inplace=True)
        frames2 = [data_new, self.target_data]
        self.data_regres = pd.concat(frames2, axis=1, sort=False)

        # convert data_matrix to dataframe for visualisation
        # self.data_vis = pd.DataFrame(
        #     self.data_matrix, columns=self.column_names)

    def Scaling_decision(self, ch_num):
        if(ch_num == 1):
            self.data_matrix = self.z_score_standardization(self.data_matrix)
            print('The data has been z-score standardized')
        if(ch_num == 2):
            self.data_matrix = self.max_min_normalization(self.data_matrix)
            print('The data has been max-min normalized')

    def Noise_detection(self):
        noise = []
        cols = self.analysis_data.columns
        for i in range(len(cols)):
            k = 0
            series = Series(self.analysis_data[cols[i]])
            stats = statsmodels.stats.diagnostic.acorr_ljungbox(
                series, lags=None, boxpierce=False)
            vals = stats[1]
            if(vals.any() <= 0.05):
                k = 1
            if(k == 1):
                noise.append(cols[i])
        if(len(noise) == 0):
            self.no = 0
            print('All features are devoid of White Gaussian and Gaussian Noise')
        else:
            self.no = 1
            # With Delimiter
            print('The numerical features with Gaussian White Noise are:!',end="")
            for each in noise:
            	print(each)

    def PCA(self, f):
        self.d = 0
        X = self.data_matrix
        cov_matrix = np.dot(X.T, X)/self.data_matrix.shape[0]
        e1, e2 = eig(cov_matrix)
        e1 = abs(e1)
        e2 = e2.T
        idx = np.argsort(e1)[::-1]
        e2 = e2[:, idx]
        e2 = e2[:, 0:f]
        e1_sort = np.sort(e1)[::-1]
        self.data_matrix_reduced = np.matmul(X, e2)
        sum1 = sum(e1_sort)
        sum_break = 0
        for i in range(f):
            sum_break += e1_sort[i]
        self.retention = round((sum_break/sum1)*100, 2)
        print('Percentage retention of features on applying PCA (linear transformation): '+str(self.retention))
        print("")
        self.Final_Concatenation()
        self.compression = round(100*((self.data_matrix.shape[0]*self.data_matrix.shape[1] - (self.data_matrix_reduced.shape[0]
                                                                                              * self.data_matrix_reduced.shape[1] + e2.shape[0]*e2.shape[1]))/(self.data_matrix.shape[0]*self.data_matrix.shape[1])), 2)
        print('Percentage reduction or compression in the storage of data: ' +
              str(self.compression)+' %')

    def Auto_Encoder(self, features):
        self.d = 1
        X = self.data_matrix
        data_count = X.shape[0]
        f = features
        value = X.shape[1]
        input_value = Input(shape=(value,))
        hidden_value = int(0.80*(value))
        encoded_1 = Dense(hidden_value, activation='sigmoid')(input_value)
        encoded = Dense(f, activation='relu')(encoded_1)
        decoded_1 = Dense(hidden_value, activation='sigmoid')(encoded)
        decoded = Dense(value, activation='sigmoid')(decoded_1)
        autoencoder = Model(input_value, decoded)
        encoder = Model(input_value, encoded)
        autoencoder.compile(optimizer='adadelta', loss='mean_squared_error')
        autoencoder.fit(X, X,
                        epochs=500,
                        batch_size=int(data_count/5),
                        shuffle=True)
        self.data_matrix_reduced = encoder.predict(X)
        org = self.data_matrix.shape[0]*self.data_matrix.shape[1]
        # new = latent + weight_component
        new = self.data_matrix_reduced.shape[0]*self.data_matrix_reduced.shape[1] +             self.data_matrix.shape[1]*self.data_matrix_reduced.shape[1]
        self.comp = round(100*((org - new)/org), 2)
        print("")
        self.Final_Concatenation()
        x_pred = autoencoder.predict(X)
        self.error = round(np.mean(np.square(X - x_pred)), 2)
        print('Percentage reduction or compression in the storage of data: ' +
              str(self.comp)+' %')
        print("")
        print('Mean Squared Error between the original data and the reconstruction of the compressed data representation: '+str(self.error))

    def Dim_Reduction(self, dim_ch, features):
        f = features
        if(dim_ch == 1):
            self.PCA(f)
        elif(dim_ch == 2):
            self.Auto_Encoder(f)

    def Final_Concatenation(self):
        self.X1 = pd.DataFrame(self.data_matrix_reduced)
        self.Y1 = self.target_data
        frames = [self.X1, self.Y1]
        self.data_final = pd.concat(frames, axis=1, sort=False)

    def Linear_Regression_model(self, X, Y):
        print("")
        xTrain, xTest, yTrain, yTest = train_test_split(
            X, Y, test_size=0.25, random_state=0)
        LinearRegressor = LinearRegression()
        LinearRegressor.fit(xTrain, yTrain)
        yPrediction = LinearRegressor.predict(xTest)
        # Printing the results
        print('Results of Multivariate Regression')
        print('intercept            : \n', LinearRegressor.intercept_)
        print('Coefficients         : \n', LinearRegressor.coef_)
        # print('Mean squared error   : %.2f' % mean_squared_error(yTest, yPrediction))
        print('Root Mean squared error   : %.2f' %
              np.sqrt(np.mean(np.square(yTest - yPrediction))))
        print('Variance score       : %.2f' % r2_score(yTest, yPrediction))
        return yTest, yPrediction

    def Logistic_Regression_model(self, X, Y):
        print("")
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
        diag_sum = 0
        classifier = LogisticRegression(random_state=0)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        # Printing the results
        # Making the Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        for i in range(cm.shape[0]):
            diag_sum += cm[i][i]
        acc = round(100*(diag_sum/sum(sum(cm))), 2)
        print("Results of Logistic Regression")
        print("")
        print('Total test samples: '+str(sum(sum(cm))))
        print("")
        print('Accuracy: '+str(acc))
        return y_test, y_pred

#     def Exp_Regression_model(self, X, Y):
#         X_exp = np.exp(X)
#         xTrain, xTest, yTrain, yTest = train_test_split(X_exp, Y, test_size = 0.25, random_state = 0)
#         LinearRegressor = LinearRegression()
#         LinearRegressor.fit(xTrain, yTrain)
#         yPrediction = LinearRegressor.predict(xTest)
#         # Printing the results
#         print('Results for Exponential Regression')
#         print('intercept            : \n', LinearRegressor.intercept_)
#         print('Coefficients         : \n', LinearRegressor.coef_)
#         print('Mean squared error   : %.2f' % mean_squared_error(yTest, yPrediction))
#         print('Variance score       : %.2f' % r2_score(yTest, yPrediction))
#         return yTest, yPrediction

    def Regression_models(self):
        self.data_1 = self.data_regres.values  # data before preprocessing
        self.data_2 = self.data_final.values  # data after preprocessing

        X_1 = self.data_1[:, 0:(self.data_1.shape[1]-1)]
        Y_1 = self.data_1[:, (self.data_1.shape[1]-1)]
        X_2 = self.data_2[:, 0:(self.data_2.shape[1]-1)]
        Y_2 = self.data_2[:, (self.data_2.shape[1]-1)]

        if(self.target_detection == 1):
           # do multivariate / simple linear regression
            print("Analysis before data preprocessing")
            yt, y1 = self.Linear_Regression_model(X_1, Y_1)
            print("")
            print("")
            print("Analysis after complete data preprocessing")
            yt, y2 = self.Linear_Regression_model(X_2, Y_2)
            # plot graph
            plt.plot(yt, color='r', label='Real Y')  # actual y test value
            plt.plot(y1, color='g', label='Predicted Y before scaling')  # predicted y value before scaling
            plt.plot(y2, color='orange', label='Predicted Y after scaling')  # predicted y value after scaling
            plt.scatter(np.arange(yt.shape[0]), yt)
            plt.scatter(np.arange(y1.shape[0]), y1)
            plt.scatter(np.arange(y2.shape[0]), y2)
            plt.xlabel('Data set #')
            plt.ylabel('Target value')
            plt.title('Linear Regression')
            plt.legend(loc='upper left')
            plt.show()
            # plt.savefig('./images/LiR.png')

        elif(self.target_detection == 0):
            # do logistic regression
            print("Analysis before data preprocessing")
            yt, y1 = self.Logistic_Regression_model(X_1, Y_1)
            print("")
            print("")
            print("Analysis after complete data preprocessing")
            yt, y2 = self.Logistic_Regression_model(X_2, Y_2)
            # plot graph
            # plt.plot(yt, color='r', label='Real Y')  # actual y test value
            # plt.plot(y1, color='g', label='Predicted Y before scaling')  # predicted y value before scaling
            # plt.plot(y2, color='orange', label='Predicted Y after scaling')  # predicted y value after scaling
            plt.scatter(np.arange(yt.shape[0]), yt, label='Real Y')
            plt.scatter(np.arange(y1.shape[0]), y1, label='Predicted Y before scaling')
            plt.scatter(np.arange(y2.shape[0]), y2, label='Predicted Y after scaling')
            plt.xlabel('Data set #')
            plt.ylabel('Target value')
            plt.legend(loc='upper left')
            plt.title('Logistic Regression')
            plt.show()
            plt.savefig('./images/LoR.png')

    def graph_test(self):
        feat = self.data.columns
        self.box_plot(feat)

    def visualization(self,choice,features):
    	print(self.data_vis.columns)
    	if choice==1:
    		self.box_plot(features)
    	elif choice==2:
    		self.hlines_plot(features)
    	elif choice==3:
    		self.histogram_plot(features)
    	elif choice==4:
    		self.scatter_plot(features)
    	else:
    		self.line_plot(features)

    def box_plot(self, features):
        fig = plt.figure(figsize=(20, 8))

        df = self.data_vis[features]

        # plt.boxplot(df)
        # plt.ylabel("Number")

        boxplot = df.boxplot()

        my_file = './images/box_plot.jpeg'       # Name of the box plot file
        fig.savefig(my_file)
        print("Saved Box plot")

    def hlines_plot(self, features):
        fig = plt.figure(figsize=(20, 8))
        x = list(self.data_vis[features[0]])
        x = np.unique(x)
        plt.hlines(1, np.min(x)-1, np.max(x)+1)
        plt.xlim(np.min(x)-1, np.max(x)+1)
        plt.ylim(0.5, 1.5)
        y = np.ones(np.shape(x))
        plt.plot(x, y, '|', ms=40)
        xlabel = features[0]
        plt.title('HLines for ' + xlabel)


        my_file = './images/hlines_plot.jpeg'       # Name of the hlines plot file
        fig.savefig(my_file)
        print("Saved HLines plot")

    def histogram_plot(self, features):
        xlabel = features[0]
        x = list(self.data_vis[features[0]])

        fig = plt.figure(figsize=(20, 8))
        plt.hist(x, bins=20)
        plt.ylabel('No of times')
        plt.title(xlabel)

        my_file = './images/hist_plot.jpeg'       # Name of the hist plot file
        fig.savefig(my_file)
        print("Saved hist plot")

    def scatter_plot(self, features):
        xlabel = features[0]
        ylabel = features[1]
        x = list(self.data_vis[features[0]])
        y = list(self.data_vis[features[1]])
        fig = plt.figure(figsize=(20, 8))
        plt.scatter(x, y, alpha=0.5)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(xlabel+" vs "+ylabel)

        my_file = './images/scatter_plot.jpeg'       # Name of the scatter plot file
        fig.savefig(my_file)
        print("Saved Scatter plot")

    # def line_plot(self, features):
    #     xlabel = features[0]
    #     ylabel = features[1]
    #     x = list(self.data_vis[features[0]])
    #     y = list(self.data_vis[features[1]])
    #     fig = plt.figure(figsize=(20, 8))

    #     plt.plot(x, y)
    #     plt.xlabel(xlabel)
    #     plt.ylabel(ylabel)
    #     plt.title(xlabel+" vs "+ylabel)

    #     my_file = './images/line_plot.jpeg'       # Name of the line plot file
    #     fig.savefig(my_file)
    #     print("Saved Line plot")

    def report(self):
        print('Data Report')
        print("")
        print('Total Rows in the original dataset: '+str(self.data.shape[0]))
        print("")
        print('Total Columns in the original dataset: ' +
              str(self.data.shape[1]))
        print("")
        print("")
        print('Target Feature Name: ' +
              str(self.data_final.columns[len(self.data_final.columns)-1]))
        print("")
        if(self.target_detection == 0):
            print('Target Feature Type: Categorical')
        if(self.target_detection == 1):
            print('Target Feature Type: Numerical')
        print("")
        if(self.d == 0):
            print('Data compression technique used: PCA (Linear)')
            print("")
            print('Percentage retention of features achieved: ' +
                  str(self.retention)+' %')
            print("")
            print('Percentage compression achieved on the Data: ' +
                  str(self.compression)+' %')
            print("")
            print("")
        if(self.d == 1):
            print('Data compression technique used Auto Encoder (Non Linear)')
            print("")
            print('Mean Squared Error between the original data and the reconstruction of the compressed data representation: '+str(self.error)+' %')
            print("")
            print('Percentage compression achieved on the Data: ' +
                  str(self.comp)+' %')
            print("")
            print("")
        print('Final Conclusions')
        print("")
        print("")
        if(self.no == 0):
            print('The features are free from any noise or deviations')
            print("")
        if(self.no == 1):
            print(
                'The features are noisy. Thus noise elimination techniques need to be employed to the data')
            print("")
        if(self.multicol == 0):
            print('The features are devoid of any Multicollinearity issues. Hence, regression models can be used for prediction.')
        elif(self.multicol == 1):
            print('The features face Multicollinearity issues. Hence regression models should not be applied directly.')

    def preview(self, counter_value):
        if(counter_value == 1 or counter_value == 2):
            print(self.data_preview)
        elif(counter_value == 3):
            if(self.flag1 == 0):
                print(self.merged_data)
            elif(self.flag1 == 1):
                fr = [self.merged_data, self.target_var]
                merge = pd.concat(fr, axis=1, sort=False)
                print(merge)
        elif(counter_value == 4 or counter_value == 5 or counter_value ==6 or counter_value==7):
            self.fr2 = [pd.DataFrame(self.data_matrix), self.target_data]
            self.new_preview = pd.concat(self.fr2, axis=1, sort=False)
            self.new_preview.columns = self.col_preview
            print(self.new_preview)
        elif(counter_value == 8 or counter_value == 9 or  counter_value ==10):
            print(self.data_final)
            
def store_obj(filename, obj):
    pickle_file = open(filename, "wb")
    pickle.dump(obj, pickle_file)
    pickle_file.close()


def load_obj(filename):
    pickle_file = open(filename, "rb")
    obj = pickle.load(pickle_file)
    pickle_file.close()
    return obj

if __name__ == '__main__':
    arg = int(sys.argv[1])
    if arg == 0:
        myAnalysis = Analysis(sys.argv[2], int(sys.argv[3]))
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 1:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Entry()
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 2:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.cat_to_num(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 3:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.MVD(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 4:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Scaling_decision(int(sys.argv[2]))
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 5:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Multicollinearity_Analysis()
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 6:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Noise_detection()
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 7:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Dim_Reduction(int(sys.argv[2]), int(sys.argv[3]))
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 8:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.Regression_models()
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 9:
        myAnalysis = load_obj(pickle_filename)
        myAnalysis.visualization(int(sys.argv[2]),sys.argv[3:])
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1
    elif arg == 99:
        myAnalysis = load_obj(pickle_filename)
        print(round(0.8*(len(myAnalysis.data.columns)-1)))
        store_obj(pickle_filename, myAnalysis)
        counter_value += 1

