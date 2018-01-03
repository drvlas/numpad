#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module implementing Numerical Pad
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from Ui_NumPad import Ui_NumPad
from Tables import *

class NumPad(QDialog, Ui_NumPad):
    def __init__(self, parent=None):
        super(NumPad, self).__init__(parent)
        self.setupUi(self)
        self.newVal = 0     # All pars are integer inside
        self.point = -1     # Point used only to format
        self.sign = 1
        self.virgin = True
        self.answer = ()
        self.showVal()
        
    def passArgs(self, minVal, maxVal, oldVal, pnt, sgn):
        self.minVal = minVal
        self.maxVal = maxVal
        self.oldVal = oldVal
        self.point = pnt
        self.sign = sgn
        self.Range_label.setText("{:d} .. {:d}".format(minVal, maxVal))
    
    @pyqtSlot()     # Don't see any difference...
    def on_pushButton0_pressed(self): self.digitPressed(0)
    @pyqtSlot()
    def on_pushButton1_pressed(self): self.digitPressed(1)
    def on_pushButton2_pressed(self): self.digitPressed(2)
    def on_pushButton3_pressed(self): self.digitPressed(3)
    def on_pushButton4_pressed(self): self.digitPressed(4)
    def on_pushButton5_pressed(self): self.digitPressed(5)
    def on_pushButton6_pressed(self): self.digitPressed(6)
    def on_pushButton7_pressed(self): self.digitPressed(7)
    def on_pushButton8_pressed(self): self.digitPressed(8)
    def on_pushButton9_pressed(self): self.digitPressed(9)
    
    def on_Del_pushButton_pressed(self): 
        self.defloration()
        self.newVal //= 10      # Right shift
        if self.point >= 0: self.point -= 1
        self.showVal()
        
    def on_pushButtonPnt_pressed(self):
        self.defloration()
        self.point = 0          # Ha! You may resetle point!
        self.showVal()
    
    def on_pushButtonSign_pressed(self):
        self.defloration()
        self.sign = -self.sign
        self.showVal()
    
    @pyqtSlot()        
    def on_Yes_pushButton_pressed(self):
        print("Yes")
        self.answer = (1, self.newVal, self.point, self.sign)
        self.close()
        return
    
    @pyqtSlot()    
    def on_No_pushButton_pressed(self):
        print("No")
        self.answer = (0, 0, 0, 0)
        self.close()
        return
    
    def digitPressed(self, d):
        self.defloration()
        self.newVal = 10*self.newVal + d
        if self.point >= 0:
            self.point += 1
        self.showVal()
        
    def showVal(self):
        print(self.newVal)
        form = point10Power[self.point][FORMAT_POS]
        shft = point10Power[self.point][RIGHT_SHIFT]
        self.newVal_label.setText(form.format(shft*self.sign*self.newVal))
        
    def defloration(self):
        if self.virgin: 
            self.newVal = 0
            self.virgin = False
        
    def results(self, good, val, pnt, sgn):
        return (good, val, pnt, sgn)
        
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    numPad = NumPad()
    numPad.exec_()
    print("Result:")
    print(numPad.answer)
    numPad.close()
    sys.exit(app.exec_())
