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

def plotsplit(X):
	x = []
	y = []
	z = []

	for i in range(0,len(X)):
		v = X[i,0].split()
		x.append(float(v[0]))
		y.append(float(v[1]))
		z.append(float(v[2]))

	return x,y,z

#data visualization
def display3D(x,y,z,p,s):
	# print(len(y),len(x))
	x = list(set(x))
	y = list(set(y))
	x = np.array(x)
	y = np.array(y)
	z = np.array(z)

	x, y = np.meshgrid(x, y)
	# print(x)
	# print(y)
	fig = plt.figure()
	ax = plt.axes(projection = '3d')
	# ax.plot3D(x,y,z)
	Z = []
	v = []
	# print(len(z))
	for i in range(0,len(z)):
		v.append(z[i])

		if(((i+1)%p) == 0):
			# print(v)
			Z.append(np.array(v))
			v = []

	Z = np.array(Z)
	# print(len(Z))
	# # print(type(Z))
	# # ax.contour3D(x, y, Z)
	ax.plot_surface(x,y,Z,rstride=1, cstride=1, cmap='viridis', edgecolor='none')
	ax.set_xlabel('R1')
	ax.set_ylabel('R2')
	ax.set_zlabel('Energy')
	# # plt.contour(x,y,Z)
	plt.title(s)
	plt.show()

	return x,y,Z


#Data preprocessing
# x,y,z = plotsplit(Xtrain)
# print(x)
# p = 30
# display3D(x,y,z,p,"Train")


#gaussian fitting 
# x = np.array(x)
# z = np.array(z)
# print(x)
# print(z)
# #uncomment the kernel which you wnt to use.
# kernel = ExpSineSquared(length_scale=1, periodicity=0.8, length_scale_bounds=(1e-05, 100000.0), periodicity_bounds=(1e-05, 100000.0))\
#     + WhiteKernel(noise_level=2, noise_level_bounds=(1e-10, 1e+1))
kernel = 1.0 * RBF(length_scale=1, length_scale_bounds=(1e-3, 1e3))\
    + WhiteKernel(noise_level=1, noise_level_bounds=(1e-10, 1e+1))
# # # kernel = DotProduct(sigma_0=1.0, sigma_0_bounds=(1e-05, 100000.0))

x_train,  y_train = datasplit(Xtrain)
gp = GaussianProcessRegressor(kernel=kernel,alpha=0.00001).fit(x_train, y_train)

# print(gp.score(x_train,y_train))

test_data = pd.read_csv('fort128.txt')
Xtest = test_data.values

# print(len(Xtest))
x_test, y_test = datasplit(Xtest)

y_pred = gp.predict(x_test)



p = 128
file = open("predict.txt","w")
# file.write("R1 \t R2 \t Energy \n")
for i in range(0,len(y_pred)):
	if((i)%p==0):
		file.write("\n")
	file.write("%.8f \t %.8f \t %.8f \n" % (x_test[i][0],x_test[i][1],y_pred[i]))

file.close()
# print(x_test[:,0])
display3D(x_test[:,0],x_test[:,1],y_pred,p,"predicted")
# print(len(x_test))
print("MSE = ",mean_squared_error(y_test,y_pred))
# print(len(x_test),len(y_pred))
# display3D(x_test[:,0],x_test[:,1],y_test,p,"Test")