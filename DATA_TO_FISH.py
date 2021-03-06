# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FBALrJ3HqU8aA3GYoIbRugvzMNMANpWj

#IMPORTING THE DATASET
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""#READING THE DATASET"""

dataset=pd.read_csv('DATA_TO_FISH.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
print(X)
print(Y)

"""#SPLITTING THE DATASET"""

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

"""#TRAINING THE DATASET"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

"""#PREDICTING THE VALUES"""

Y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2) #prints no. with 2 decimal place
#printing the predictions and actual data in order to compare them
print(np.concatenate((Y_pred.reshape(len(Y_pred),1),Y_test.reshape(len(Y_test),1)),1))

"""#COEFFICIENT AND INTERCEPT"""

print(regressor.coef_)
print(regressor.intercept_)