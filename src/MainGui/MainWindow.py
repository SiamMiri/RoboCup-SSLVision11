# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 382)
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lbl_University = QtWidgets.QLabel(self.centralwidget)
        self.lbl_University.setGeometry(QtCore.QRect(500, 0, 171, 61))
        self.lbl_University.setObjectName("lbl_University")
        self.lbl_University.setStyleSheet("background-image : url(src/MainGui/logo_th_rosenheim.png)")
        
        self.btn_LoadImageFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_LoadImageFile.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.btn_LoadImageFile.setObjectName("btn_LoadImageFile")
        self.btn_StartImageCapturing = QtWidgets.QPushButton(self.centralwidget)
        self.btn_StartImageCapturing.setGeometry(QtCore.QRect(20, 130, 181, 31))
        self.btn_StartImageCapturing.setObjectName("btn_StartImageCapturing")
        self.btn_StartVideoCapturing = QtWidgets.QPushButton(self.centralwidget)
        self.btn_StartVideoCapturing.setGeometry(QtCore.QRect(460, 130, 181, 31))
        self.btn_StartVideoCapturing.setObjectName("btn_StartVideoCapturing")
        self.btn_ImageColorConfiguration = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ImageColorConfiguration.setGeometry(QtCore.QRect(20, 180, 181, 31))
        self.btn_ImageColorConfiguration.setObjectName("btn_ImageColorConfiguration")
        self.txt_FilePath = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_FilePath.setGeometry(QtCore.QRect(150, 80, 491, 31))
        self.txt_FilePath.setObjectName("txt_FilePath")
        self.lbl_version = QtWidgets.QLabel(self.centralwidget)
        self.lbl_version.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.lbl_version.setObjectName("lbl_version")
        self.btn_VideoColorConfiguration = QtWidgets.QPushButton(self.centralwidget)
        self.btn_VideoColorConfiguration.setGeometry(QtCore.QRect(460, 180, 181, 31))
        self.btn_VideoColorConfiguration.setObjectName("btn_VideoColorConfiguration")
        self.lbl_NumFrameToSave = QtWidgets.QLabel(self.centralwidget)
        self.lbl_NumFrameToSave.setGeometry(QtCore.QRect(20, 260, 181, 17))
        self.lbl_NumFrameToSave.setObjectName("lbl_NumFrameToSave")
        # self.lbl_NumRoboImageToSave = QtWidgets.QLabel(self.centralwidget)
        # self.lbl_NumRoboImageToSave.setGeometry(QtCore.QRect(20, 300, 221, 16))
        # self.lbl_NumRoboImageToSave.setObjectName("lbl_NumRoboImageToSave")
        self.txt_NumFrameToSave = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_NumFrameToSave.setGeometry(QtCore.QRect(250, 250, 91, 31))
        self.txt_NumFrameToSave.setObjectName("txt_NumFrameToSave")
        # self.txt_NumRoboImageToSave = QtWidgets.QTextEdit(self.centralwidget)
        # self.txt_NumRoboImageToSave.setGeometry(QtCore.QRect(250, 290, 91, 31))
        # self.txt_NumRoboImageToSave.setObjectName("txt_NumRoboImageToSave")
        
        self.checkBox_ShowRobotsInfo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ShowRobotsInfo.setGeometry(QtCore.QRect(400, 250, 241, 21))
        self.checkBox_ShowRobotsInfo.setObjectName("checkBox_ShowRobotsInfo")
        
        self.checkBox_SaveFrame = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_SaveFrame.setGeometry(QtCore.QRect(400, 280, 241, 21))
        self.checkBox_SaveFrame.setObjectName("checkBox_SaveFrame")
        
        self.checkBox_ConnectServer = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ConnectServer.setGeometry(QtCore.QRect(400, 310, 241, 21))
        self.checkBox_ConnectServer.setObjectName("checkBox_ConnectServer")
        
        self.lbl_ServerInformation = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ServerInformation.setGeometry(QtCore.QRect(230, 130, 141, 17))
        self.lbl_ServerInformation.setObjectName("lbl_ServerInformation")
        self.lbl_Port = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Port.setGeometry(QtCore.QRect(230, 160, 201, 16))
        self.lbl_Port.setObjectName("lbl_Port")
        self.lbl_Group = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Group.setGeometry(QtCore.QRect(230, 190, 201, 16))
        self.lbl_Group.setObjectName("lbl_Group")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_University.setText(_translate("MainWindow", ""))
        self.btn_LoadImageFile.setText(_translate("MainWindow", "Image Path"))
        self.btn_StartImageCapturing.setText(_translate("MainWindow", "Start Processing Image"))
        self.btn_StartVideoCapturing.setText(_translate("MainWindow", "Start Processing Video"))
        self.btn_ImageColorConfiguration.setText(_translate("MainWindow", "Configure Color for Image"))
        self.lbl_version.setText(_translate("MainWindow", "version: 1.2.2"))
        self.btn_VideoColorConfiguration.setText(_translate("MainWindow", "Configure Color for  Video"))
        self.lbl_NumFrameToSave.setText(_translate("MainWindow", "Number of frame to save:"))
        #self.lbl_NumRoboImageToSave.setText(_translate("MainWindow", "Number of robot image to save:"))
        self.checkBox_ShowRobotsInfo.setText(_translate("MainWindow", "Show Robot Information on Frame"))
        self.checkBox_SaveFrame.setText(_translate("MainWindow", "Save Frame"))
        self.checkBox_ConnectServer.setText(_translate("MainWindow", "Start sendeing data"))
        self.lbl_ServerInformation.setText(_translate("MainWindow", "Server Information:"))
        self.lbl_Port.setText(_translate("MainWindow", "Port:"))
        self.lbl_Group.setText(_translate("MainWindow", "Group:"))
