import serial
import serial.tools.list_ports as list_ports
from PyQt5 import QtCore, QtGui, QtWidgets

from mainWindow_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.onLoadWindow()

    def onLoadWindow(self):
        self.actionSeleccionarPuerto.setEnabled(False)
        self.addPorts()
        self.menuPuertos.triggered.connect(self.portChecked)
        self.conectarArduino.triggered.connect(self.tryConnectArduino)
        self.conectarArduino.setEnabled(False)

    def tryConnectArduino(self):
        print("Conectando a arduino")
        self.arduinoStatus = "connecting"
        self.serialArduino = serial.Serial(self.arduinoPort, 9600)
        rawString = self.serialArduino.readline()
        print(rawString.decode('ascci'))
        self.serialArduino.close()

    def addPorts(self):
        portList=list_ports.comports()
        for port in portList:
            portAction =  QtWidgets.QAction(port.device,self)
            portAction.setCheckable(True)
            self.menuPuertos.addAction(portAction)
            print("Port added:"+port.device)

    def portChecked(self, checkedAction):
        if checkedAction.isChecked():
            self.arduinoPort=checkedAction.text()
            print("Puerto seleccionado:"+self.arduinoPort)
            self.menuPuertos.setTitle("Puerto: "+self.arduinoPort)
            for actionItem in self.menuPuertos.actions():
                if actionItem.text()!=self.arduinoPort:
                    actionItem.setChecked(False)
            self.conectarArduino.setEnabled(True)
        else:
            print("Puerto no seleccionado:"+self.arduinoPort)
            self.arduinoPort=""
            self.menuPuertos.setTitle("Puerto")
            self.conectarArduino.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
