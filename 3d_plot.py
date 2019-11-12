
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np




NUM_PUNTOS=32
NUM_HALF=16

#   Cambio variable
aux=[]
aux=arange(NUM_HALF,NUM_PUNTOS,1)
aux=np.append(aux,arange(0,NUM_HALF,1))
print(aux)


def interpole(X,Y):
    x=x_data[aux]
    y=y_data[aux]
    #print(x)
    z=[]
    for i in range (0,NUM_PUNTOS/2):
        zn=[]
        for j in range(0,NUM_PUNTOS):
            
            zn.append((y[i]*(NUM_HALF-abs(NUM_HALF-j))/NUM_HALF)/2+(x[j]*(NUM_HALF-abs(NUM_HALF-i))/NUM_HALF)/2)
            #print("zn",zn)
        z.append(zn)
    print("z",shape(z))
    return z




x_data=np.load("s21_x.npy")
y_data=np.load("s21_y.npy")
#print(x_data)
z=interpole(x_data,y_data)















fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()