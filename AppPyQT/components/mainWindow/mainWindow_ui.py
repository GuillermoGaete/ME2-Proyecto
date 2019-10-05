# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 461)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 181))
        self.groupBox.setObjectName("groupBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuPrincipal = QtWidgets.QMenuBar(MainWindow)
        self.menuPrincipal.setGeometry(QtCore.QRect(0, 0, 796, 22))
        self.menuPrincipal.setObjectName("menuPrincipal")
        self.menuArchivo = QtWidgets.QMenu(self.menuPrincipal)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuDispositivos = QtWidgets.QMenu(self.menuPrincipal)
        self.menuDispositivos.setObjectName("menuDispositivos")
        self.menuArduino = QtWidgets.QMenu(self.menuDispositivos)
        self.menuArduino.setObjectName("menuArduino")
        MainWindow.setMenuBar(self.menuPrincipal)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionConectar = QtWidgets.QAction(MainWindow)
        self.actionConectar.setObjectName("actionConectar")
        self.actionj_2 = QtWidgets.QAction(MainWindow)
        self.actionj_2.setObjectName("actionj_2")
        self.actionCOM_1 = QtWidgets.QAction(MainWindow)
        self.actionCOM_1.setObjectName("actionCOM_1")
        self.actionDesconectar = QtWidgets.QAction(MainWindow)
        self.actionDesconectar.setEnabled(False)
        self.actionDesconectar.setObjectName("actionDesconectar")
        self.actionPuerto = QtWidgets.QAction(MainWindow)
        self.actionPuerto.setEnabled(True)
        self.actionPuerto.setObjectName("actionPuerto")
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArduino.addAction(self.actionConectar)
        self.menuArduino.addAction(self.actionDesconectar)
        self.menuArduino.addAction(self.actionPuerto)
        self.menuDispositivos.addSeparator()
        self.menuDispositivos.addAction(self.menuArduino.menuAction())
        self.menuPrincipal.addAction(self.menuArchivo.menuAction())
        self.menuPrincipal.addAction(self.menuDispositivos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Estado dispositivos"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuDispositivos.setTitle(_translate("MainWindow", "Dispositivos"))
        self.menuArduino.setTitle(_translate("MainWindow", "Arduino"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionConectar.setText(_translate("MainWindow", "Conectar"))
        self.actionj_2.setText(_translate("MainWindow", "j"))
        self.actionCOM_1.setText(_translate("MainWindow", "COM 1"))
        self.actionDesconectar.setText(_translate("MainWindow", "Desconectar"))
        self.actionPuerto.setText(_translate("MainWindow", "Puerto"))


