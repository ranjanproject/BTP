import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.gaussian_process import GaussianProcessRegressor 
from sklearn.gaussian_process.kernels import ExpSineSquared,RBF, WhiteKernel, DotProduct, Matern


#data input
data = pd.read_csv('fort2.txt')
X = data.values

# print(X)
x = []
y = []
z = []
for i in range(0,len(X)):
	v = X[i,0].split()
	x.append(float(v[0]))
	y.append(float(v[1]))
	z.append(float(v[2]))

# print(x[0],y[0])
#data visualization

def display3D(x,y,z,p):
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
	for i in range(0,len(z)):
		v.append(z[i])

		if(((i+1)%p) == 0):
			# print(v)
			Z.append(np.array(v))
			v = []

	Z = np.array(Z)
	# print(Z)
	# print(type(Z))
	# ax.contour3D(x, y, Z)
	ax.plot_surface(x,y,Z,rstride=1, cstride=1, cmap='viridis', edgecolor='none')
	ax.set_xlabel('R1')
	ax.set_ylabel('R2')
	ax.set_zlabel('Energy')
	plt.contour(x,y,Z)
	plt.show()

	return


#Data preprocessing
display3D(x,y,z,40)
# print(x[0])
