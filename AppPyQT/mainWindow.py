import serial
import serial.tools.list_ports as list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QThreadPool, pyqtSignal, pyqtSlot
from pyudev import Context, Monitor, MonitorObserver
from qtpy.QtCore import Qt, QFileSystemWatcher, QSettings, Signal

from ui.mainWindow_ui import *
from lib.controllers.arduinoController import arduinoController
import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter('[%(threadName)s][%(name)s] - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)
logger.propagate = False

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ttyDeviceEvent = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.threadpool=QThreadPool()
        #Controller to manage Arduino
        self.arduinoController=arduinoController(self.threadpool)
        self.selectedPort=''
        #TODO conect arduinoController signals to MainWindow slots

        #levantamos el detector de coneccion/desconeccion
        self.context = Context()
        self.monitor = Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='tty')
        self.observer = MonitorObserver(self.monitor, callback=self.eventDetected, name='monitor-observer')
        self.observer.daemon
        self.observer.start()
        self.ttyDeviceEvent.connect(self.onTtyDeviceEvent)
        logger.info("MonitorObserver started")

        self.onLoadWindow()

    def onLoadWindow(self):
        portList=list_ports.comports()
        for port in portList:
            portAction = QtWidgets.QAction(port.device,self)
            portAction.setCheckable(True)
            self.menuPuertos.addAction(portAction)

        self.actionSeleccionarPuerto.setEnabled(False)
        self.enviarComando.clicked.connect(self.sendCommand)
        self.conectarArduino.setEnabled(False)

        self.menuPuertos.triggered.connect(self.onPortClicked)
        self.conectarArduino.triggered.connect(self.arduinoController.connectArduino)

    def sendCommand(self):
        text=self.comando.text()
        logger.debug("Enviando comando:"+text)

    def removePorts(self):
        logger.debug("TODO: Remove ports on arduinoEventDetected")
        self.checkConnection()

    @pyqtSlot(QtWidgets.QAction)
    def onPortClicked(self,port):
        logger.info('Port: {} - check status: {}'.format(port.text(),port.isChecked()))
        if port.isChecked():
            self.selectedPort=port.text()
            self.menuPuertos.setTitle('Puerto: {}'.format(self.selectedPort))
            for actionItem in self.menuPuertos.actions():
                if actionItem.text()!=self.selectedPort:
                    actionItem.setChecked(False)
        else:
            if self.selectedPort==port.text():
                self.selectedPort=""
                self.menuPuertos.setTitle('Puerto')
        logger.info('Selected port: {}'.format(self.selectedPort))


    @pyqtSlot(str)
    def onTtyDeviceEvent(self,action):
        if action =="added":
            portList=list_ports.comports()
            for port in portList:
                portAction = QtWidgets.QAction(port.device,self)
                portAction.setCheckable(True)
                isPresent = False;
                for actionItem in self.menuPuertos.actions():
                    if actionItem.text()==port.device:
                        logger.info("Port added already present")
                        isPresent=True
                if isPresent==False:
                    logger.info("New port added")
                    self.menuPuertos.addAction(portAction)
        elif action =="removed":
            logger.info("Do something on removed device")
            if self.arduinoController.isConnected()==False:
                logger.info("Arduino not conected")
                self.removePorts()
                portList=list_ports.comports()]\
                nothingSelected = True
                for port in portList:
                    portAction = QtWidgets.QAction(port.device,self)
                    portAction.setCheckable(True)
                    if self.selectedPort==port.device:
                        nothingSelected = False
                        logger.info("Reload selected port")
                        portAction.setChecked(True)
                    self.menuPuertos.addAction(portAction)
                if nothingSelected==True:
                    self.selectedPort=""
                    self.menuPuertos.setTitle('Puerto')
                    logger.info('Selected port: {}'.format(self.selectedPort))


    #Este evento se dispara en el MonitorObserver Thread
    def eventDetected(self,device):
        logger.info('Event detected - DEVICE: {0} - ACTION: {0.action}'.format(device))
        if device.action =="add":
            self.ttyDeviceEvent.emit("added")
        if device.action =="remove":
            self.ttyDeviceEvent.emit("removed")

    def removePorts(self):
        self.menuPuertos.clear()
        actionSeleccionarPuerto = QtWidgets.QAction("Seleccionar Puerto",self)
        actionSeleccionarPuerto.setEnabled(False)
        font = QtGui.QFont()
        actionSeleccionarPuerto.setFont(font)
        actionSeleccionarPuerto.setObjectName("actionSeleccionarPuerto")
        actionSeleccionarPuerto.setText("Seleccionar Puerto")
        self.menuPuertos.addAction(actionSeleccionarPuerto)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
