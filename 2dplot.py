

import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import math
import traceback
import sys
import serial
import serial.tools.list_ports as list_ports
from tempfile import TemporaryFile


NUM_PUNTOS=32








x_data=np.load("s21_x.npy")
y_data=np.load("s21_y.npy")



print("Generando grafico polar de las mediciones tomadas")
r = np.arange(-0.75, 0.25, 1/NUM_PUNTOS)
theta = 2*np.pi*r
#db.append(db[0])

ax = plt.subplot(211, projection='polar')
ax.plot(theta, x_data)
print(np.floor((max(x_data)+10)/10))
ax.set_rmax(np.floor((max(x_data)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(x_data)/10)*10,np.floor((max(x_data)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Lobulo eje X", va='bottom')


ax = plt.subplot(212, projection='polar')
ax.plot(theta, y_data)
print(np.floor((max(y_data)+10)/10))
ax.set_rmax(np.floor((max(y_data)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(y_data)/10)*10,np.floor((max(y_data)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Lobulo eje Y", va='bottom')
plt.show(block=True)
