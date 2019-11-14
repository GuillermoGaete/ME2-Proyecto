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



#rm = visa.ResourceManager('@py')



#   Simulacion



medidasim=[-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-44,-44,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30]



## Simulacion End



#print('******------ Lista de recursos -----*******')
#
#resources = rm.list_resources()
#
#print(resources)

# resources es una tupla de los distintos "endpoints"

#for resource in resources:
#
#    result = resource.find('tty')
#
#    if result>0:
#
#        print("no valido")
#
#    else:
#
#        myInstrument=rm.open_resource(resource)
#
#        idnResponse = myInstrument.query('*IDN?')
#
#        print ("Resourcer number: "+str(resources.index(resource)),"\n\t|-->VISA resource name: "+str(resource))
#
#        print("\t|-->Instrument: "+idnResponse)

#=======
    #print(resources)
    ## resources es una tupla de los distintos "endpoints"
    #
    #myInstrument = rm.open_resource(resources[0])
    #idnResponse = myInstrument.query('*IDN?')
    #print ("Resourcer number: "+str(resources.index(resources[0])),"\n\t|-->VISA resources[0] name: "+str(resources[0]))
    #print("\t|-->Instrument: "+idnResponse)
    #
    #
    #>>>>>>> Stashed changes

##

def reset_position():

    serialArduino.write(b'z')

    responseSerial=""

    serialArduino.write(order.encode())

    while(responseSerial!="finish"):

        readedLine=serialArduino.readline()

        responseSerial = readedLine.decode().rstrip()

        print(responseSerial)



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

print("            Inicializando VNA            ")

#send_command('INST "NA";*OPC?')

#send_command("CALC:PAR:COUN 1")

#send_command("CALC:PAR:DEF S21")

print("Seteando medicion S21, con centro en 2.15E9")

#send_command("FREQ:CENT 2.15E9")

#send_command("FREQ:SPAN 500E6")

##send_command("FREQ:STAR 1E9")

##send_command("FREQ:STOP 3E9")

print("Activando Marker")

#send_command("CALC:MARK1:ACTivate")

#send_command("CALC:MARK1 NORM")

#send_command("CALC:MARK1:X 2.15E9")



print("Configurando IFBW y promediado")

#send_command("BWID 10E3")

#send_command("AVER:COUN 12")

#send_command("AVER:CLE")





NUM_PUNTOS=int(32)

NUM_MEDIOGIRO=int(NUM_PUNTOS/2)



db=[]

portList=list_ports.comports()

print("Listado de puertos:")

for port in portList:

    print("Port added:"+port.device)



input("Press Enter to continue...")



serialArduino = serial.Serial('/dev/ttyACM0', 9600)

readedLine=serialArduino.readline()

print(readedLine.decode().rstrip())





print("     Lectura del valor patron    ")

f=open("dbiset.txt","r")

dbistr=f.readline()

if len(dbistr) is 0:

    print("No hay o no pudo leerse el valor patron con el que se va a medir")

    exit()

else:

    dbi=float(dbistr)

    print("El valor patron es de:", dbi)



order="r"

reset_position()

data=np.load("s21_x.npy")
print("Datos simulados:",data)
for x in range(0, NUM_MEDIOGIRO):

    res=data[x]

    ##send_command("AVER:CLE")
#
    #print(res)
#
    #print(type(res))
#
    #resultlist=res.split(',')
#
    #print(resultlist)
#
    #aux=resultlist[0].split('E+')
#
    #if(len(aux)<2):
#
    #    aux=resultlist[0].split('E-')
#
    #print(len(aux))
#
    #aux2=float(aux[0])*math.pow(10,float(aux[1]))
#
    ##directivity=int(round(10*aux2))
#
    #
#
    #print("Valor medido",aux2)

    directivity=res

    db.append(directivity)

    serialArduino.write(b'r')

    responseSerial=""

    serialArduino.write(order.encode())

    while(responseSerial!="finish"):

        readedLine=serialArduino.readline()

        responseSerial = readedLine.decode().rstrip()

        print(responseSerial)

serialArduino.write(b'z')

responseSerial=""

serialArduino.write(order.encode())

while(responseSerial!="finish"):

    readedLine=serialArduino.readline()

    responseSerial = readedLine.decode().rstrip()

    print(responseSerial)

for x in range(0,NUM_MEDIOGIRO):

    serialArduino.write(b'l')

    responseSerial=""

    serialArduino.write(order.encode())

    while(responseSerial!="finish"):

        readedLine=serialArduino.readline()

        responseSerial = readedLine.decode().rstrip()

        print(responseSerial)

    

for x in range(0, NUM_MEDIOGIRO):



    res=data[x+NUM_MEDIOGIRO]

#    send_command("AVER:CLE")
#
#    print(res)
#
#    print(type(res))
#
#    resultlist=res.split(',')
#
#    print(resultlist)
#
#    aux=resultlist[0].split('E+')
#
#    if(len(aux)<2):
#
#        aux=resultlist[0].split('E-')
#
#    print(len(aux))
#
#    res=float(aux[0])*math.pow(10,float(aux[1]))

    #directivity=int(round(10*aux2))

    

    print("Valor medido",res)

    directivity=res

    db.append(directivity)

    serialArduino.write(b'r')

    responseSerial=""

    serialArduino.write(order.encode())

    while(responseSerial!="finish"):

        readedLine=serialArduino.readline()

        responseSerial = readedLine.decode().rstrip()

        print(responseSerial)

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







#print("\nSaving [db] data to s21_x.npy\n")
#
#outfile = TemporaryFile()
#
#np.save("s21_x.npy",db)
#
#_ = outfile.seek(0)
#
#print("Saved file:",np.load("s21_x.npy"))





print("Generando grafico polar de las mediciones tomadas")

r = np.arange(-0.75, 0.25, 1/NUM_PUNTOS)

theta = 2*np.pi*r

print(db)

#db.append(db[0])

ax = plt.subplot(111, projection='polar')

ax.plot(theta, db)



print(np.floor((max(db)+10)/10))

ax.set_rmax(np.floor((max(db)+10)/10)*10)

ax.set_rticks(np.arange(np.floor(min(db)/10)*10,np.floor((max(db)+10)/10)*10,10))  # Less radial ticks

ax.set_rlabel_position(90)  # Move radial labels away from plotted line

ax.grid(True)



ax.set_title("Radiation lobule of a patch antenna", va='bottom')

plt.show(block=True)



#send_command("CALC:MARK:BWID:DATA?")
