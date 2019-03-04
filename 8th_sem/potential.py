import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor 
from sklearn.gaussian_process.kernels import ExpSineSquared,RBF, WhiteKernel, DotProduct, Matern
#data reading from file
df = pd.read_excel('morse2.xlsx')
data = df.values
X = data[:,0]
Y = data[:,1]
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)
# print(X,Y)
plt.scatter(X,Y,color="red",label='Training data')
plt.legend(loc=2)
# plt.show()
# #uncomment the kernel which you wnt to use.
# kernel = ExpSineSquared(length_scale=1.0, periodicity=1.0, length_scale_bounds=(1e-05, 100000.0), periodicity_bounds=(1e-05, 100000.0))
# kernel = 2.0 * RBF(length_scale=50, length_scale_bounds=(1e-2, 1e3))\
#     + WhiteKernel(noise_level=1, noise_level_bounds=(1e-10, 1e+1))
# kernel = DotProduct(sigma_0=1.0, sigma_0_bounds=(1e-05, 100000.0))
# plt.scatter(X,Y)
kernel=Matern(length_scale=1.0, length_scale_bounds=(1e-05, 100000.0), nu=1)
def fun(y_mean):
	f = open('test2.txt','w')
	for i in range(0,len(y_mean)):
		f.write(str(y_mean[i][0])+"\n")

	f.close()


def RMSE(ytest,y_mean):
	sm=0;
	for i in range(0,len(ytest)):
		sm = sm + (ytest[i]-y_mean[i])**2
		sm = np.sqrt(sm/(len(y_mean)))

	print('RMSE =',sm)




#genrating 500 points between 1 to 15 
# X_ = np.linspace(1, 15, 100)
# df = pd.read_excel('data.xlsx')
# test = df.values
# X_ = test[:,0]
# # X_ = X_.reshape(-1,1)
# ytest = test[:,1]
# print(X_,ytest)
# # print(X_)
# df = pd.read_fwf('test.txt')
df = pd.read_csv('test.txt',header=None)
Xn = df.values
# # X_ = list(X_)
X_=[]
for i in range(0,len(Xn)):
	X_.append(Xn[i][0])

X_ = np.asarray(X_)


df = pd.read_csv('test3.txt',header=None)
ytest = df.values


gp = GaussianProcessRegressor(kernel=kernel,alpha=0.00001).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=0.00001')

gp = GaussianProcessRegressor(kernel=kernel,alpha=0.001).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=0.001')

gp = GaussianProcessRegressor(kernel=kernel,alpha=0.1).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=0.1')

gp = GaussianProcessRegressor(kernel=kernel,alpha=0.5).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=0.5')

gp = GaussianProcessRegressor(kernel=kernel,alpha=1).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=1')

gp = GaussianProcessRegressor(kernel=kernel,alpha=2).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=2')

gp = GaussianProcessRegressor(kernel=kernel,alpha=3).fit(X, Y)
y_mean, y_cov = gp.predict(X_[:, np.newaxis], return_cov=True)
fun(y_mean)
RMSE(ytest,y_mean)
plt.plot(X_,y_mean,label='alpha=3')

plt.legend(loc=4)
plt.show()
