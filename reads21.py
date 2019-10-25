#Deberia poder sin cambiarle el nombre pero tengo otro paquete llamado visa instalado
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import math
import traceback
import sys
import serial
import serial.tools.list_ports as list_ports

rm = visa.ResourceManager()

print('******------ Lista de recursos -----*******')
resources = rm.list_resources()
# resources es una tupla de los distintos "endpoints"
for resource in resources:
    myInstrument = rm.open_resource(resource)
    idnResponse = myInstrument.query('*IDN?')
    print ("Resourcer number: "+str(resources.index(resource)),"\n\t|-->VISA resource name: "+str(resource))
    print("\t|-->Instrument: "+idnResponse)




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

send_command('INST "NA";*OPC?')
send_command("CALC:PAR:COUN 1")
send_command("CALC:PAR:DEF S21")
send_command("FREQ:CENT 2.15E9")
send_command("FREQ:SPAN 1E9")
#send_command("FREQ:STAR 1E9")
#send_command("FREQ:STOP 3E9")
send_command("CALC:MARK1:ACTivate")
send_command("CALC:MARK1 NORM")
send_command("CALC:MARK1:X 2.15E9")


NUM_PUNTOS=100

db=[]

portList=list_ports.comports()
print("Listado de puertos:")
for port in portList:
    print("Port added:"+port.device)


for x in range(0, NUM_PUNTOS):
    res=send_command("CALC:MARK1:Y?")
    print(res)
    print(type(res))
    resultlist=res.split(',')
    print(resultlist)
    aux=resultlist[0].split('E+')
    aux2=float(aux[0])*math.pow(10,float(aux[1]))
    directivity=int(round(10*aux2))
    print(directivity)

    db.append(directivity)

#Asumo que ACA hay que mover el arduino
    #Hay que reemplazar COM4 por el puerto
    serialArduino = serial.Serial('COM4', 9600)
    #Enviamos r para que se mueva a la derecha
    serialArduino.write(b'r')
    #Nos quedamos leyendo, si arduino no contesta nada aca se traba
    readedLine=serialArduino.readline()

    print(readedLine.decode().rstrip())
    #cerramos la conexion serie
    serialArduino.close()
##Aca termina lo de Arduino

    input("Press Enter to continue...")

r = np.arange(0, 1, 1/NUM_PUNTOS)
theta = 2*np.pi*r
print(db)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, db)
ax.set_rmax(0)
ax.set_rticks(np.arange(-600,0,100))  # Less radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Radiation lobule of a patch antenna", va='bottom')
plt.show()
#send_command("CALC:MARK:BWID:DATA?")
