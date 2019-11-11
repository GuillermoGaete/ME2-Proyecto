#Deberia poder sin cambiarle el nombre pero tengo otro paquete llamado visa instalado
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import math
import traceback
import sys
import serial
import serial.tools.list_ports as list_ports
from tempfile import TemporaryFile


#   Simulacion

medidasim=[float(-30),float(-31),float(-32),float(-33),float(-34),float(-35),float(-36),float(-37),float(-38),float(-39),float(-40),float(-41),float(-42),float(-43),float(-44),float(-44),float(-44),float(-44),float(-43),float(-42),float(-41),float(-40),float(-39),float(-38),float(-37),float(-36),float(-35),float(-34),float(-33),float(-32),float(-31),float(-30)]

## Simulacion End


def send_command(com):
    command=""
    command = com
    lastChar = command[len(command)-1]
    if lastChar != '?':
        response = myInstrument.write(command)
    else:
        response = myInstrument.query(command)
    print('Comando ingresado:',command)
    print('Response:',response)
    return response
print("\n            Inicializando VNA            \n")
#send_command('INST "NA";*OPC?')
#send_command("CALC:PAR:COUN 1")
#send_command("CALC:PAR:DEF S21")
print("\nSeteando medicion S21, con centro en 2.15E9\n")
#send_command("FREQ:CENT 2.15E9")
#send_command("FREQ:SPAN 1E9")
#send_command("FREQ:STAR 1E9")
#send_command("FREQ:STOP 3E9")
print("\nActivando Marker\n")
#send_command("CALC:MARK1:ACTivate")
#send_command("CALC:MARK1 NORM")
#send_command("CALC:MARK1:X 2.15E9")
print("\n             Inicializacion terminada            \n")

NUM_PUNTOS=32

db=[]

#portList=list_ports.comports()
#print("Listado de puertos:")
#for port in portList:
#    print("Port added:"+port.device)
#
#input("Press Enter to continue...")
#
#serialArduino = serial.Serial('/dev/ttyACM1', 9600)
#readedLine=serialArduino.readline()
#print(readedLine.decode().rstrip())


print("     Lectura del valor patron    ")
f=open("aux.txt","r")
dbistr=f.readline()
if len(dbistr) is 0:
    print("No hay o no pudo leerse el valor patron con el que se va a medir")
    exit()
else:
    dbi=int(dbistr)
    print("El valor patron es de:", dbi)

order="r"
for x in range(0, NUM_PUNTOS):
    res=medidasim[x]
    directivity=res
    print("Valor medido",directivity)
    directivity=directivity-dbi
    db.append(directivity)
    #input("Press Enter to continue...")

#Asumo que ACA hay que mover el arduino
    #Hay que reemplazar COM4 por el puerto
    #serialArduino = serial.Serial('/dev/ttyACM0', 9600)
    #print(1)
    #Enviamos r para que se mueva a la derecha
    #serialArduino.write(b'r')
    #Nos quedamos leyendo, si arduino no contesta nada aca se traba
    #print(2)
    
    #readedLine=serialArduino.readline()
    #print(readedLine.decode().rstrip())
    #cerramos la conexion serie
    #serialArduino.close()
##Aca termina lo de Arduino


print("\nSaving [db] data to outfile.npy\n")
outfile = TemporaryFile()
np.save("outfile.npy",db)
_ = outfile.seek(0)
print("Loaded file",np.load("outfile.npy"))






print("\nGenerando grafico polar de las mediciones tomadas\n")
r = np.arange(-0.75, 0.25, 1/NUM_PUNTOS)
theta = 2*np.pi*r
print(db)
print(theta)
#db.append(db[0])
ax = plt.subplot(111, projection='polar')
ax.plot(theta, db)

print(np.floor((max(db)+10)/10))
ax.set_rmax(np.floor((max(db)+10)/10)*10)
ax.set_rticks(np.arange(np.floor(min(db)/10)*10,np.floor((max(db)+10)/10)*10,10))  # Less radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from plotted line
ax.grid(True)
ax.set_title("Radiation lobule of a patch antenna", va='bottom')

plt.show()


#send_command("CALC:MARK:BWID:DATA?")
