# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analiz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import   QMessageBox
from mplwidget1 import MplWidget1
from mplwidget2 import MplWidget2
from mplwidget3 import MplWidget3
from mplwidget4 import MplWidget4

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import  serial 
import time
import threading

#global ser
#ser = Serial()
sys_name = "Arduino"
global ser
ser = serial.Serial('COM6', baudrate=9600, timeout=10,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 704)
        MainWindow.setWindowIcon(QtGui.QIcon("robot.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MplWidget1 = MplWidget1(self.centralwidget)
        self.MplWidget1.setGeometry(QtCore.QRect(220, 10, 521, 301))
        self.MplWidget1.setObjectName("MplWidget1")
        self.MplWidget2 = MplWidget2(self.centralwidget)
        self.MplWidget2.setGeometry(QtCore.QRect(790, 10, 521, 301))
        self.MplWidget2.setObjectName("MplWidget2")
        self.MplWidget3 = MplWidget3(self.centralwidget)
        self.MplWidget3.setGeometry(QtCore.QRect(220, 360, 521, 301))
        self.MplWidget3.setObjectName("MplWidget3")
        self.MplWidget4 = MplWidget4(self.centralwidget)
        self.MplWidget4.setGeometry(QtCore.QRect(790, 360, 521, 301))
        self.MplWidget4.setObjectName("MplWidget4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1190, 640, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 570, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 610, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 61, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 160, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 200, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(60, 320, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 350, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 380, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 240, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 61, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 280, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 420, 51, 31))
        self.label_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 450, 51, 31))
        self.label_8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 480, 51, 31))
        self.label_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 510, 51, 31))
        self.label_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_data1 = QtWidgets.QLabel(self.centralwidget)
        self.label_data1.setGeometry(QtCore.QRect(120, 420, 51, 31))
        self.label_data1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data1.setObjectName("label_data1")
        self.label_dat2 = QtWidgets.QLabel(self.centralwidget)
        self.label_dat2.setGeometry(QtCore.QRect(120, 450, 51, 31))
        self.label_dat2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_dat2.setObjectName("label_dat2")
        self.label_data4 = QtWidgets.QLabel(self.centralwidget)
        self.label_data4.setGeometry(QtCore.QRect(120, 510, 51, 31))
        self.label_data4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data4.setObjectName("label_data4")
        self.label_data3 = QtWidgets.QLabel(self.centralwidget)
        self.label_data3.setGeometry(QtCore.QRect(120, 480, 51, 31))
        self.label_data3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data3.setObjectName("label_data3")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(20, 10, 171, 131))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_img.setPixmap(QtGui.QPixmap("robot.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.t1 =np.array([],dtype=int)
        self.signal1 =np.array([],dtype=int)
        self.signal2 =np.array([],dtype=int)
        self.signal3 =np.array([],dtype=int)
        self.signal4 =np.array([],dtype=int)
        self.i =0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda:self.baglan())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ULUSOY ROBOTIC INTERFACE 1.0"))
        self.label.setText(_translate("MainWindow", "ULUSOY ROBOTİC INTERFACE 1.0"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.pushButton.setText(_translate("MainWindow", "BAĞLAN"))
        self.pushButton_2.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.label_3.setText(_translate("MainWindow", "BAUD RATE"))
        self.radioButton.setText(_translate("MainWindow", "ARDUİNO"))
        self.radioButton_2.setText(_translate("MainWindow", "ESP 8266"))
        self.radioButton_3.setText(_translate("MainWindow", "RASPBERRY"))
        self.label_5.setText(_translate("MainWindow", "PARİTY"))
        self.label_6.setText(_translate("MainWindow", "TİMEOUT"))
        self.label_7.setText(_translate("MainWindow", "DATA1 ="))
        self.label_8.setText(_translate("MainWindow", "DATA2 ="))
        self.label_9.setText(_translate("MainWindow", "DATA3 ="))
        self.label_10.setText(_translate("MainWindow", "DATA4 ="))
        self.label_data1.setText(_translate("MainWindow", "........."))
        self.label_dat2.setText(_translate("MainWindow", "........."))
        self.label_data4.setText(_translate("MainWindow", "........."))
        self.label_data3.setText(_translate("MainWindow", "........."))
        self.comboBox.addItems(["COM6"])
        self.comboBox_2.addItems(["9600"])
        self.comboBox_3.addItems(["NONE"])
        self.comboBox_4.addItems(["1000(MS)"])

    def update_graph(self,data1,data2,data3,data4):

        self.i = self.i + 1
        self.t1=np.append(self.t1, self.i)
        self.signal1=np.append(self.signal1, data1)
        self.signal2=np.append(self.signal2, data2)
        self.signal3=np.append(self.signal3, data3)
        self.signal4=np.append(self.signal4, data4)
        
        self.MplWidget1.canvas.axes.clear()
        self.MplWidget1.canvas.axes.plot(self.t1, self.signal1)
        self.MplWidget1.canvas.axes.legend(('d1'),loc='upper right')
        self.MplWidget1.canvas.axes.set_title('DATA1 Signal')
        self.MplWidget1.canvas.draw()
        
        
        self.MplWidget2.canvas.axes.clear()
        self.MplWidget2.canvas.axes.plot(self.t1, self.signal2)
        self.MplWidget2.canvas.axes.legend(('d2'),loc='upper right')
        self.MplWidget2.canvas.axes.set_title('DATA2 Signal')
        self.MplWidget2.canvas.draw()

        self.MplWidget3.canvas.axes.clear()
        self.MplWidget3.canvas.axes.plot(self.t1,self.signal3)
        self.MplWidget3.canvas.axes.legend(('d3'),loc='upper right')
        self.MplWidget3.canvas.axes.set_title('DATA3 Signal')
        self.MplWidget3.canvas.draw()

        self.MplWidget4.canvas.axes.clear()
        self.MplWidget4.canvas.axes.plot(self.t1,self.signal4)
        self.MplWidget4.canvas.axes.legend(('d4'),loc='upper right')
        self.MplWidget4.canvas.axes.set_title('DATA4 Signal')
        self.MplWidget4.canvas.draw()

    def baglan(self):
        
        self.timeout = 0
        self.check_serial_event()

    def check_serial_event(self):

        self.timeout += 1
        serial_thread = threading.Timer(1, self.check_serial_event)
        if ser.is_open == True:
            serial_thread.start()
            if ser.in_waiting:
                eol = b'\n'
                leneol = len(eol)
                line = bytearray()
                line =ser.readline()
                line = line.rstrip()
                distance = line.decode("utf-8")
                data = distance.split(",")
                self.label_data1.setText(str(data[0]))
                self.label_dat2.setText(str(data[1]))
                self.label_data3.setText(str(data[2]))
                self.label_data4.setText(str(data[3]))
                self.update_graph(data[0],data[1],data[2],data[3])
                print (distance)
                self.timeout = 0

        if self.timeout >= 10:
            ser.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
