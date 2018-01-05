#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Main executable module
"""
from PyQt5 import QtWidgets
from ui.window import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
