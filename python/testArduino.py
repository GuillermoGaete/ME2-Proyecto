import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import math
import traceback
import sys
import serial
import serial.tools.list_ports as list_ports

#Hay que reemplazar por el puerto
serialArduino = serial.Serial('/dev/ttyACM0', 9600)
#Enviamos r para que se mueva a la derecha
readedLine=serialArduino.readline()
print(readedLine.decode().rstrip())

r="n"
while(r!="e"):
    r=input("Order to arduino:")
    serialArduino.write(r.encode())
    readedLine=serialArduino.readline()
    print("Arduino response:"+readedLine.decode().rstrip())
    ##Aca termina lo de Arduino

serialArduino.close()
