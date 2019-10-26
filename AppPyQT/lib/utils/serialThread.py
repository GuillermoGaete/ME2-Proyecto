from PyQt5.QtCore import QThread
import logging

class serialThread(QThread):
    def __init__(self, portname="", baudrate=0):
        QThread.__init__(self)
        self.portname, self.baudrate = portname, baudrate
        self.loggerName = "SerialThread"
        self.logger("Created..")
        logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
        logging.warning('This is a Warning')

    def setPort(self,port):
        self.portname=port

    def setBaudrate(self,baudrate):
        self.baudrate=baudrate

    def run(self):
        self.logger("Starting thread..")

    def logger(self,message):
        print('[{}] - {}'.format(self.loggerName,message))
