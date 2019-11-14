

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



#todos los valores estan normalizados para un patron seteado a mano




x5_data=np.load("./medidas/estrutcura1_32_X1.npy")
x7_data=np.load("./medidas/estrutcura1_32_X2.npy")
x8_data=np.load("./medidas/estrutcura1_32_X3.npy")

y1_data=np.load("./medidas/estrutcura1_32_X1.npy")
y2_data=np.load("./medidas/estrutcura1_32_X2.npy")
y3_data=np.load("./medidas/estrutcura1_32_X3.npy")

t=np.arange(0,NUM_PUNTOS,1)

scipy.io.savemat('testX.mat', dict(x=t, y=x5_data))
scipy.io.savemat('testY.mat', dict(x=t, y=y1_data))



print("Generando grafico polar de las mediciones tomadas")
r = np.arange(-0.75, 0.25, 1/NUM_PUNTOS)
theta = 2*np.pi*r-(90/180)*np.pi
#db.append(db[0])

ax = plt.subplot(211, projection='polar')
ax.plot(theta, x5_data,'r')
ax.plot(theta, x7_data,'g')
ax.plot(theta, x8_data,'b')

print(np.floor((max(x5_data)+10)/10))
ax.set_rmax(np.floor((max(x5_data)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(x5_data)/10)*10,np.floor((max(x5_data)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Lobulo eje X", va='bottom')


ax = plt.subplot(212, projection='polar')
ax.plot(theta, y1_data,'r')
ax.plot(theta, y2_data,'g')
ax.plot(theta, y3_data,'b')

print(np.floor((max(y1_data)+10)/10))
ax.set_rmax(np.floor((max(y1_data)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(y1_data)/10)*10,np.floor((max(y1_data)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Lobulo eje Y", va='bottom')
plt.show(block=True)
