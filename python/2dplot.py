

import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import math
import traceback
import sys
import serial
import serial.tools.list_ports as list_ports
from tempfile import TemporaryFile
import numpy as np
import scipy.io

NUM_PUNTOS=32
NUM_PUNTOS128=128


#todos los valores estan normalizados para un patron seteado a mano




x5_data=np.load("../medidas/estrutcura_viernes_128_X1.npy")
x7_data=np.load("../medidas/estrutcura_viernes_128_X2.npy")
x8_data=np.load("../medidas/estrutcura_viernes_32_X3.npy")

y1_data=np.load("../medidas/estrutcura_viernes_128_Y1.npy") #Valor medido con 128
y2_data=np.load("../medidas/estrutcura_viernes_128_Y2.npy") #Valor medido con 128
y3_data=np.load("../medidas/estrutcura_viernes_32_Y3.npy")

print(max(y1_data),max(x5_data))
dif=abs(x5_data[0]-y1_data[0])

if x5_data[0]<y1_data[0]:
    x5_data=np.add(x5_data,dif)
    x7_data=np.add(x7_data,dif)
else:
    y1_data=np.add(y1_data,dif)
    y2_data=np.add(y2_data,dif)


print("     Lectura del valor patron    ")
f=open("dbiset.txt","r")
dbistr=f.readline()
if len(dbistr) is 0:
    print("No hay o no pudo leerse el valor patron con el que se va a medir")
    exit()
else:
    dbi=float(dbistr)
    print("El valor patron es de:", dbi)

patron=6.32-dbi


x5_data=np.add(x5_data,patron)
x7_data=np.add(x7_data,patron)
x8_data=np.add(x8_data,patron)
y1_data=np.add(y1_data,patron)
y2_data=np.add(y2_data,patron)
y3_data=np.add(y3_data,patron)



print(max(x5_data))

t=np.arange(0,NUM_PUNTOS,1)

scipy.io.savemat('../MATLAB/estrutcura_viernes_dbi128X.mat', dict(x=t, y=x5_data))
scipy.io.savemat('../MATLAB/estrutcura_viernes_dbi128Y.mat', dict(x=t, y=y1_data))



print("Generando grafico polar de las mediciones tomadas")
r = np.arange(-0.75, 0.25, 1/NUM_PUNTOS)
theta = 2*np.pi*r-(90/180)*np.pi
r2 = np.arange(-0.75, 0.25, 1/NUM_PUNTOS128)
theta2 = 2*np.pi*r2-(90/180)*np.pi
#db.append(db[0])

ax = plt.subplot(211, projection='polar')
ax.set_theta_zero_location("N")
ax.plot(theta2, x5_data,'r')
ax.plot(theta2, x7_data,'g')
#ax.plot(theta, x8_data,'b')

print(np.floor((max(x5_data)+10)/10))
ax.set_rmax(np.floor((max(x5_data)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(x5_data)/10)*10,np.floor((max(x5_data)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(0)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Lobulo eje X [dBi]", va='bottom')


ax = plt.subplot(212, projection='polar')
ax.set_theta_zero_location("N")
ax.plot(theta2, y1_data,'r')
ax.plot(theta2, y2_data,'g')
#ax.plot(theta, y2_data,'g')
#ax.plot(theta, y3_data,'b')

print(np.floor((max(y1_data)+10)/10))
ax.set_rmax(np.floor((max(y1_data)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(y1_data)/10)*10,np.floor((max(y1_data)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(0)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Lobulo eje Y [dBi]", va='bottom')
plt.show(block=True)
