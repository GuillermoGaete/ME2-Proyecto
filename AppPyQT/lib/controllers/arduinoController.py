from PyQt5.QtCore import QThread
from pyudev import Context, Monitor, MonitorObserver
from qtpy.QtCore import Qt, QFileSystemWatcher, QSettings, Signal
import serial
import serial.tools.list_ports as list_ports
from lib.utils.serialThread import serialThread

class arduinoController(QThread):
    ''' Monitor udev for detection of usb '''
    eventDectected = Signal(str)

    def __init__(self):
        ''' Initiate the object '''
        QThread.__init__(self)
        self.loggerName = 'arduinoController'
        self.connectionStatus='idle'
        self.port=""
        self.logger("Created..")


    def __del__(self):
        self.wait()

    def onEventDetected(self,device):
        self.logger('Event detected - DEVICE: {0} - ACTION: {0.action}'.format(device))
        if device.action =="add":
            self.eventDectected.emit("added")
        if device.action =="remove":
            self.eventDectected.emit("removed")

    def run(self):
        #levantamos el detector de coneccion/desconeccion
        self.context = Context()
        self.monitor = Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='tty')
        self.observer = MonitorObserver(self.monitor, callback=self.onEventDetected, name='monitor-observer')
        self.observer.daemon
        self.observer.start()
        #levantamos el thread que se comunica por serie
        self.serial = serialThread()
        self.serial.start()


    def connect(self):
        if(self.port!=""):
            self.logger("Try to connect arduino")
            #Hacer esto con un QThead
            self.serialArduino = serial.Serial(self.port, 9600)
            self.serialArduino.write(b'r')
            readedLine=self.serialArduino.readline()
            response = readedLine.decode().rstrip()
            self.logger('Response: {}'.format(response))
            if(response=='ack'):
                self.status='connected'
                #emitir una senial
                self.logger('Connected')


    def setPort(self,port):
        self.port=port
        self.logger('Port selected: {0}'.format(self.port))

    def deletePort(self):
        self.logger('Port deleted: {0}'.format(self.port))
        self.setPort("")

    def logger(self,message):
        print('[{}] - {}'.format(self.loggerName,message))
