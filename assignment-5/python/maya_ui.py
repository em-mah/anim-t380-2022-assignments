from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance 

# Get a reference to the main Maya application window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget) 

class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
        
        # Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        # Set the UI display title and size    
        self.setWindowTitle('My Maya Widget')        
        self.setGeometry(50, 50, 350, 150)
        
              
        self.my_button = QPushButton('Cylinders', self)
        self.my_button.clicked.connect(self.button_onClicked)   
        
        self.button_2 = QPushButton('Cubes', self)
        self.button_2.move(0,50)
        self.button_2.clicked.connect(self.button_2_onClicked)
        
        self.new_button = QPushButton('Exit', self)
        self.new_button.move(0,100)
        self.new_button.clicked.connect(self.close)

         
    def button_onClicked(self):
        for i in range(5):
            n = 2-(2/5)*i
            cmds.polyCylinder(h=1, r=n)
            cmds.move(0,0.5+i,0)
        print("Clicked!")
        
    def button_2_onClicked(self):
        for i in range(5):
            n = 3-(3/5)*i
            cmds.polyCube(h=1, d=n, w=n)
            cmds.move(0,0.5+i,0)
        print("Clicked!")
        
my_widget = MyMayaWidget()     
my_widget.show()