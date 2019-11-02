from PyQt5.QtCore import QThread, QThreadPool,QRunnable,pyqtSlot,pyqtSignal,Q_FLAG
from PyQt5 import QtWidgets
from qtpy.QtCore import Qt, QFileSystemWatcher, QSettings, Signal, QObject
import serial
import serial.tools.list_ports as list_ports
from lib.utils.serialThread import serialThread
import logging
import time

# Create a custom logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_format = logging.Formatter('[%(threadName)s][%(name)s] - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)
logger.propagate = False

class arduinoController(QObject):

    connecting = pyqtSignal()
    error = pyqtSignal(tuple)

    result = pyqtSignal(object)

    class statusConnection:
        IDLE = 0x00
        CONNECTING = 0x01
        CONNECTED = 0x02
        WAITING_ACK = 0x03
        DISCONNECTING = 0x04
        DISCONECTED = 0x05
        ERROR = 0x06

    Q_FLAG(statusConnection)

    def __init__(self,threadPool):
        super(arduinoController, self).__init__()
        logger.debug("created")
        self.threadPool=threadPool
        self.status=self.statusConnection.IDLE
        self.port=''
        self.serialThread=serialThread()
        self.threadPool.start(self.serialThread)

    def __del__(self):
        logger.info("in __del__ method")

    def isConnected(self):
        if self.status==self.statusConnection.CONNECTED:
            return True
        else:
            return False

    @pyqtSlot()
    def connectArduino(self):
        logger.debug('CONNECTING')
        self.status=self.statusConnection.CONNECTING
        self.connecting.emit()

'''
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
'''
