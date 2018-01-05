#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""

# from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from qt_window import Ui_Window
from numpad import Numpad
from tables import *


class MainWindow(QMainWindow, Ui_Window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.counter = 0
        self.val = 1234
        self.mi = -9999
        self.ma = 9999
        self.point = 2
        self.sign = 1
        self.show_val()
        
    def show_val(self):
        value = self.val * point10Power[self.point][RIGHT_SHIFT]
        if self.sign == -1: value = -value
        form = point10Power[self.point][FORMAT_POS]
        self.lab_val.setText(form.format(value))
        
    #@pyqtSlot()
    def on_pb_modify_pressed(self):
        self.counter += 1
        self.lab_cnt.setText("{:d}".format(self.counter))
        np = Numpad(mi=self.mi, ma=self.ma, va=self.val, po=self.point, si=self.sign)
        np.exec_()
        print(np.answer)    # DEBUG
        np.close()
        if (len(np.answer) != 0) and (np.answer[VALID] == 1):
            val = np.answer[VAL]
            point = np.answer[PNT]
            sign = np.answer[SGN]
            if point < 0:
                point = 0           # Value -1 means zero (as no point was pressed)
            if point > self.point:
                mult = point10Power[point-self.point][RIGHT_SHIFT]
                val *= mult
            elif point < self.point:
                mult = point10Power[self.point - point][LEFT_SHIFT]
                val *= int(mult)
            a_half = 0.5
            if sign == -1:
                val = -val
                a_half = -0.5
            if val < self.mi:
                self.val = self.mi
            elif val > self.ma:
                self.val = self.ma
            else:
                self.val = int(val+a_half)
        self.show_val()
         
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
