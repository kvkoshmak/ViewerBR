# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:49:14 2018

@author: KV_1
"""
import sys
from PyQt5.QtWidgets import (QMainWindow,QFileDialog, QAction, QTextEdit,
 QInputDialog, QPushButton, QApplication, QLineEdit)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        OpenButton = QPushButton("Open", self)
        OpenButton.move(30, 50)
        
        self.txt = QTextEdit("Qline", self)
        self.txt.move(300, 50)
        self.txt.resize(300, 300);

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
        btn2.clicked.connect(self.showDialog)
      
        OpenButton.clicked.connect(self.showOpenDialog)            
        OpenButton.setStatusTip('Open new File')
        
        self.statusBar()
        
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showOpenDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)  
        
        self.setGeometry(300, 300, 690, 500)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.txt.setText(sender.text())
        
    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.txt.setText(str(text))
 
    def showOpenDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.txt.setText(data)  
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    ex = Example()
    app.exec_()