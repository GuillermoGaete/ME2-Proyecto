#Deberia poder sin cambiarle el nombre pero tengo otro paquete llamado visa instalado
import pyvisa as visa
rm = visa.ResourceManager()

print('******------ Lista de recursos -----*******')
resources = rm.list_resources()
# resources es una tupla de los distintos "endpoints"
for resource in resources:
    myInstrument = rm.open_resource(resource)
    idnResponse = myInstrument.query('*IDN?')
    print ("Resourcer number: "+str(resources.index(resource)),"\n\t|-->VISA resource name: "+str(resource))
    print("\t|-->Instrument: "+idnResponse)


print('******------ Test de comandos -----*******')
print('Se pueden probar comandos, desde: http://na.support.keysight.com/fieldfox/help/Programming/webhelp/FFProgrammingHelp.htm')
print('Para salir ingresar: exit\n')
#myInstrument = rm.open_resource('USB0::10893::23576::MY56072049::0::INSTR')

command=""
try:
    while command != 'exit':
        command = input("Comando: ")
        lastChar = command[len(command)-1]
        if lastChar != '?':
            response = myInstrument.write(command)
        else:
            response = myInstrument.query(command)
        print('Comando ingresado:',command)
        print('Response:',response)
except Exception as e:
    print (e)
