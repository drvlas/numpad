# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ParTxt_label = QtWidgets.QLabel(self.centralwidget)
        self.ParTxt_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ParTxt_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ParTxt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ParTxt_label.setObjectName("ParTxt_label")
        self.horizontalLayout.addWidget(self.ParTxt_label)
        self.ParVal_label = QtWidgets.QLabel(self.centralwidget)
        self.ParVal_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ParVal_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ParVal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ParVal_label.setObjectName("ParVal_label")
        self.horizontalLayout.addWidget(self.ParVal_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Modify_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Modify_pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Modify_pushButton.setObjectName("Modify_pushButton")
        self.verticalLayout.addWidget(self.Modify_pushButton)
        self.Counter_label = QtWidgets.QLabel(self.centralwidget)
        self.Counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Counter_label.setObjectName("Counter_label")
        self.verticalLayout.addWidget(self.Counter_label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 26))
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
        self.ParTxt_label.setText(_translate("MainWindow", "Value"))
        self.ParVal_label.setText(_translate("MainWindow", "Entered"))
        self.Modify_pushButton.setText(_translate("MainWindow", "Modify"))
        self.Counter_label.setText(_translate("MainWindow", "Counter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

