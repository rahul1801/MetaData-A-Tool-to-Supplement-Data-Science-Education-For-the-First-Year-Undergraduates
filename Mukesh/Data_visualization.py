'''
data_visual is the dataframe from which we have to extract columns.
eg
column1 = list(data_visual['columname'])
here, 'features', the parameter passed to all functions is the list of column names for which the graph is plotted.
'''


import numpy as np  
import pandas as pd
import os
from matplotlib import pyplot as plt

def box_plot(features):
    fig = plt.figure(figsize=(20,8))
    
    df = data_visual[features]

    plt.boxplot(df)
    #plt.xlabel(features.columns[0])
    plt.ylabel("Number")

    my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
    my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
    my_file = 'box_plot.jpeg'       # Name of the scatter plot file
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
    my_file = 'hlines_plot.jpeg'       # Name of the scatter plot file
    fig.savefig(os.path.join(my_path, my_file))

    print("Saved HLines plot")

def histogram_plot(features):
    
    #xlabel =features.columns[0]
    #x = features.iloc[:,1]
    xlabel = features[0]
    x = list(data_visual[features[0]])
    
    fig = plt.figure(figsize=(20,8))
    plt.hist(x,bins=20)
    plt.ylabel('No of times')
    plt.title(xlabel)

    my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
    my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
    my_file = 'histogram_plot.jpeg'       # Name of the scatter plot file
    fig.savefig(os.path.join(my_path, my_file))
    
    print("Saved Histogram plot")

def scatter_plot(features):
    #xlabel = features.columns[0]
    #ylabel = features.columns[1]
    xlabel = features[0]
    ylabel = features[1]
    #cols = features.shape[1]
    #x = features.iloc[:,:cols-1]
    #y = features.iloc[:,cols-1:cols]
    x = list(data_visual[features[0]])
    y = list(data_visual[features[1]])
    fig = plt.figure(figsize=(20,8))
    plt.scatter(x,y,alpha=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(xlabel+" vs "+ylabel)
    
    my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
    my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
    my_file = 'scatter_plot.jpeg'       # Name of the scatter plot file
    fig.savefig(os.path.join(my_path, my_file))
    
    print("Saved Scatter plot")
    

def line_plot(features):
    xlabel = features[0]
    ylabel = features[1]
    #cols = features.shape[1]
    #x = features.iloc[:,:cols-1]
    #y = features.iloc[:,cols-1:cols]
    x = list(data_visual[features[0]])
    y = list(data_visual[features[1]])
    fig = plt.figure(figsize=(20,8))
    
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(xlabel+" vs "+ylabel)

    my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.
    my_path = os.path.dirname(my_path)  # Goes to previous directory to store the image
    my_file = 'line_plot.jpeg'       # Name of the scatter plot file
    fig.savefig(os.path.join(my_path, my_file))
    
    print("Saved Line plot")

if __name__ == '__main__':
    print("1.Box plot")
    print("2.Histogram")
    print("3.HLines")
    print("4.Scatter plot")
    print("5.Line plot")
    type_plot = int(input())
    my_path = os.path.abspath(__file__)
    features = pd.read_csv(" ")             # THE FEATURES FILE DIRECTORY MUST BE SPECIFIED OR MUST BE PASSED AS LIST
    if(type_plot == 1):
        box_plot(features)
    elif(type_plot == 2):
        histogram_plot(features)
    elif(type_plot == 3):
        hlines_plot(features)
    elif(type_plot == 4):
        scatter_plot(features)
    elif(type_plot == 5):
        line_plot(features)
    else:
        print("nothing")



