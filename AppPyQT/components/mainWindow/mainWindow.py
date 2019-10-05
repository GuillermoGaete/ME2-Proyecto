import serial
import serial.tools.list_ports as list_ports

from mainWindow_ui import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.onLoadWindow()
        
    def onLoadWindow(self):
        portList=list_ports.comports()
        for port in portList:
            mainPort = self.menuPrincipal.menuDispositivos.menuArduino.menuPort
            print(port.device)
            print(mainMenu)
            mainMenu.addMenu('File')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
