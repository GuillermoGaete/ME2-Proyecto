import serial
import serial.tools.list_ports as list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

from ui.mainWindow_ui import *
from lib.controllers.arduinoController import arduinoController

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.arduinoController=arduinoController()
        self.arduinoController.start()
        self.arduinoController.eventDectected[str].connect(self.arduinoEventDetected)
        self.onLoadWindow()


    def arduinoEventDetected(self,action):
        if action == "removed":
            if(self.arduinoPort!=""):
                self.arduinoController.checkConnection()

        if action == "added":
            self.menuPuertos.clear()
            self.addPorts()

    def onLoadWindow(self):
        self.addPorts()
        self.actionSeleccionarPuerto.setEnabled(False)
        self.menuPuertos.triggered.connect(self.portChecked)
        self.enviarComando.clicked.connect(self.sendCommand)
        self.conectarArduino.triggered.connect(self.arduinoController.connect)
        self.conectarArduino.setEnabled(False)

    def sendCommand(self):
        text=self.comando.text()
        print("Enviando comando:"+text)

    def removePorts(self):
        print("TODO: Remove ports on arduinoEventDetected")
        self.checkConnection()

    def addPorts(self):
        portList=list_ports.comports()
        for port in portList:
            portAction = QtWidgets.QAction(port.device,self)
            portAction.setCheckable(True)
            self.menuPuertos.addAction(portAction)

    def portChecked(self, checkedAction):
        if checkedAction.isChecked():
            self.arduinoPort=checkedAction.text()
            self.menuPuertos.setTitle("Puerto: "+self.arduinoPort)
            for actionItem in self.menuPuertos.actions():
                if actionItem.text()!=self.arduinoPort:
                    actionItem.setChecked(False)
            self.conectarArduino.setEnabled(True)
            self.arduinoController.setPort(self.arduinoPort)
        else:
            self.arduinoController.deletePort()
            self.menuPuertos.setTitle("Puerto")
            self.conectarArduino.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
