#Deberia poder sin cambiarle el nombre pero tengo otro paquete llamado visa instalado
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import math
import traceback
import sys
import serial
import serial.tools.list_ports as list_ports

rm = visa.ResourceManager('@py')

print('******------ Lista de recursos -----*******')
resources = rm.list_resources()
print(resources)
# resources es una tupla de los distintos "endpoints"

myInstrument = rm.open_resource(resources[0])
idnResponse = myInstrument.query('*IDN?')
print ("Resourcer number: "+str(resources.index(resources[0])),"\n\t|-->VISA resources[0] name: "+str(resources[0]))
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

portList=list_ports.comports()
print("Listado de puertos:")
for port in portList:
    print("Port added:"+port.device)

res=send_command("CALC:MARK1:Y?")
print(res)
print(type(res))
resultlist=res.split(',')
print(resultlist)
aux=resultlist[0].split('E+')
aux2=float(aux[0])*math.pow(10,float(aux[1]))
directivity=int(round(10*aux2))
print(directivity)
f=open("dbiset.txt","w+")
dirstr=str(directivity)
f.write(dirstr)
f.close