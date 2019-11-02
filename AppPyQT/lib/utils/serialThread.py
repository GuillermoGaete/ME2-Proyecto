from PyQt5.QtCore import QThread,QObject,pyqtSignal,QRunnable,pyqtSlot
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

class serialThread(QRunnable):

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(serialThread, self).__init__()
        self.args = args
        self.kwargs = kwargs
        logger.debug('serialThread created')

    @pyqtSlot()
    def run(self):
        logger.debug('serialThread started')
