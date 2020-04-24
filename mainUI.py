# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'with_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 251, 631))
        self.listWidget.setObjectName("listWidget")
        self.roilistwidget = QtWidgets.QListWidget(self.centralwidget)
        self.roilistwidget.setGeometry(QtCore.QRect(280, 650, 381, 151))
        self.roilistwidget.setObjectName("roilistwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionreadfile = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionreadfile.setIcon(icon)
        self.actionreadfile.setObjectName("actionreadfile")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionreadfile)
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionreadfile.setText(_translate("MainWindow", "读入图片"))
        self.actionreadfile.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionexit.setStatusTip(_translate("MainWindow", "点击鼠标退出系统"))
        self.actionexit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
