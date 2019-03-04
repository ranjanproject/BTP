from sklearn.datasets import make_friedman2
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import numpy as np 

# X, y = make_friedman2(n_samples=500, noise=0, random_state=0)
# X = np.delete(X, [2,3],1)

x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 100)

x, y = np.meshgrid(x, y)
print(x)

z = np.sin(np.sqrt(x**2 + y**2))
print(z)
# print(type(z[0]))
fig = plt.figure()
ax = plt.axes(projection = '3d')
# # ax.plot3D(x,y,z)
# # ax.contour3D(x, y, z, 50, cmap='binary')
ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Energy')

# plt.show()