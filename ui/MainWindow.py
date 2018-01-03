#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from Ui_MainWindow import Ui_MainWindow
from NumPad import NumPad
from Ui_NumPad import Ui_NumPad
from Tables import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.counter = 0
        self.parVal = 1234
        self.point = 2
        self.sign = 1
        self.showVal()
        
    def showVal(self):
        value = self.parVal * point10Power[self.point][RIGHT_SHIFT]
        if self.sign == -1: value = -value
        form = point10Power[self.point][FORMAT_POS]
        self.ParVal_label.setText(form.format(value))
        
    @pyqtSlot()
    def on_Modify_pushButton_pressed(self):
        self.counter += 1
        self.Counter_label.setText("{:d}".format(self.counter))
        numPad = NumPad()
        numPad.exec_()
        print(numPad.answer)    # DEBUG
        numPad.close()
        if (len(numPad.answer) != 0) and (numPad.answer[VALID] == 1):
            self.parVal = numPad.answer[VAL]
            self.point = numPad.answer[PNT]
            self.sign = numPad.answer[SGN]
        self.showVal()
         
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
