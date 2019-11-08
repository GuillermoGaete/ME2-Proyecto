
from numpy import * 	# for outer and arange
import pylab as p
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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
    for i in range (0,NUM_PUNTOS):
        zn=[]
        for j in range(0,NUM_PUNTOS):
            
            zn.append((y[i]*(NUM_HALF-abs(NUM_HALF-j)))/2+(x[j]*(NUM_HALF-abs(NUM_HALF-i)))/2)
            #print("zn",zn)
        z.append(zn)
    print("z",shape(z))
    return z




x_data=np.load("s21_x.npy")
y_data=np.load("s21_y.npy")
#print(x_data)
z=interpole(x_data,y_data)
















#fig = p.figure()	
#ax = p3.Axes3D(fig)	
#
#theta = arange(0,pi,pi/32)	
#phi = arange(0,2*pi,pi/32)	
#r = 2 * pow(math.e, -((theta**4)/(0.25**2))) # need to distort the radius by some function
#print("r",r)
#print('r',shape(r))
#x = z[16]*outer(cos(phi), sin(theta))	
#y = z[16]*outer(sin(phi), sin(theta))
#z = z[16]*outer(ones(phi.shape), cos(theta))	
#
#print (shape(x), shape(y), shape(z))
#
#ax.plot_wireframe(x,y,z)
#ax.set_xlabel("X")
#ax.set_ylabel("Y")
#ax.set_zlabel("Z")
#
#p.show()
#
#

x = np.arange(0, 32, 1)
y = np.arange(0, 32, 1)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, z, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_title('surface')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()