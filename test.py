# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:15:11 2019

@author: Pratik_Ranjan
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.gaussian_process import GaussianProcessRegressor 
from sklearn.gaussian_process.kernels import ExpSineSquared,RBF, WhiteKernel, DotProduct, Matern
from sklearn.metrics import mean_squared_error

#data input
data = pd.read_csv('fort30.txt')
Xtrain = data.values

def datasplit(X):
	x = []
	z = []
	for i in range(0,len(X)):
		v = X[i,0].split()
		xx = []
		xx.append(float(v[0]))
		xx.append(float(v[1]))
		x.append(np.array(xx))
		z.append(float(v[2]))

	x = np.array(x)
	return x,z
#from pandas import Series
X, Y = datasplit(Xtrain)

split = len(Y)/2
split = int(split)
#Y = np.log(Y)
X1, X2 = Y[0:split],Y[split:]

#print(X1.mean(),X2.mean())
#print(X1.var(),X2.var())

from statsmodels.tsa.stattools import adfuller
result = adfuller(Y)

print(result[1])