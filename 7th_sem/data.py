import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
df = pd.read_csv("fort.txt",header=None)
data = df.values
X =[]
for i in range(1,len(data)):
	X.append(data[i][0].split())

X = np.array(X);
Z = X[:,2]
X = np.delete(X,2,1)
X = X.astype(np.float)
Z = Z.astype(np.float)


x=[]
y=[]
z=[]
for i in range(0,len(X)):
	x.append(X[i][0])
	y.append(X[i][1])
	z.append(Z[i])

x = np.array(x)
y = np.array(y)
z = np.array(z)
x = x.reshape(x.shape[0],1)
y = y.reshape(y.shape[0],1)
z = z.reshape(z.shape[0],1)
# plt.plot(x,y)
# plt.show()
# print(y)
# x, y = np.meshgrid(X[:,0],X[:,1])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
plt.show()
# plt.plot(x,y)
# Axes3D.plot_surface(x,y,z,rstride=10,cstride=10) 