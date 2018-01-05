# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(240, 204)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.lab_txt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_txt.setFont(font)
        self.lab_txt.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_txt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lab_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_txt.setObjectName("lab_txt")
        self.horizontal_layout.addWidget(self.lab_txt)
        self.lab_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_val.setFont(font)
        self.lab_val.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_val.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lab_val.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_val.setObjectName("lab_val")
        self.horizontal_layout.addWidget(self.lab_val)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.pb_modify = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pb_modify.setFont(font)
        self.pb_modify.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pb_modify.setObjectName("pb_modify")
        self.verticalLayout.addWidget(self.pb_modify)
        self.lab_cnt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_cnt.setFont(font)
        self.lab_cnt.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_cnt.setObjectName("lab_cnt")
        self.verticalLayout.addWidget(self.lab_cnt)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 27))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Window"))
        self.lab_txt.setText(_translate("Window", "Value"))
        self.lab_val.setText(_translate("Window", "Entered"))
        self.pb_modify.setText(_translate("Window", "Modify"))
        self.lab_cnt.setText(_translate("Window", "Counter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

