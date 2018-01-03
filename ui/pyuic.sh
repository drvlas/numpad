#!/bin/bash
echo "Compile mainWindow.ui file to Python mainWindow.py"
pyuic5 -x Ui_MainWindow.ui -o Ui_MainWindow.py
pyuic5 -x Ui_NumPad.ui -o Ui_NumPad.py
echo "The end!"
sleep 1s
