import os, sys
import maya.cmds as mc
import maya.mel as mel
import json

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
          
        self.setWindowTitle('Rig Builder')        
        self.setGeometry(50, 50, 500, 350)
        self.resize(400, 400)
        
        self.label = QtWidgets.QLabel('Rig Builder', self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(140,20)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
              
        self.button_refModel = QPushButton('Reference Model', self)
        self.button_refModel.setGeometry(QtCore.QRect(100, 80, 200, 50))
        self.button_refModel.clicked.connect(self.refModel_onClicked)   
        
        self.button_buildRig = QPushButton('Build Rig', self)
        self.button_buildRig.setGeometry(QtCore.QRect(100, 150, 200, 50))
        self.button_buildRig.clicked.connect(self.buildRig_onClicked)
        
        self.button_reloadVer = QPushButton('Reload Version', self)
        self.button_reloadVer.setGeometry(QtCore.QRect(100, 220, 200, 50))
        self.button_reloadVer.clicked.connect(self.reloadVer_onClicked)
        
        self.button_loadTemp = QPushButton('Load Template', self)
        self.button_loadTemp.setGeometry(QtCore.QRect(100, 290, 200, 50))
        self.button_loadTemp.clicked.connect(self.loadTemp_onClicked)
            
         
    def refModel_onClicked(self):
        filePath = mc.fileDialog2(fileMode=1, caption="Reference Model")
        filename = os.path.basename(filePath[0])
        mc.file(filePath[0], r=True, mnc=False)
    
    def buildRig_onClicked(self): # runs everything
        getRigNamingConvention = open(os.path.join(os.getcwd(), 'rigNamingConvention.json'))
        RNC = json.load(getRigNamingConvention)
        self.renameLoc(RNC)
        self.createJoints(RNC)
        # Joint Definitions and Lists
        middleList = []
        rightList = []
        leftList = []

        if middleList != [] and leftList != [] and rightList != []:
            middleList = []
            leftList = []
            rightList = []
            self.classifyJoints(middleList, rightList, leftList)
        elif middleList == [] and leftList == [] and rightList == []:
            self.classifyJoints(middleList, rightList, leftList)
        else:
            print('Unable to classify joints')
        
        self.allParent(middleList, rightList, leftList)
        self.createCtrls(RNC, middleList, rightList, leftList)
        
    def reloadVer_onClicked(self):
        getfileNamingConvention = open(os.path.join(os.getcwd(), 'fileNamingConvention.json'))
        FNC = json.load(getfileNamingConvention)
        #mc.file('{task}_{type}_{model}_{version}RN'.format(**FNC), removeReference=True)
        fileFormat = '{path}{task}.{type}.{model}.{version}.{ext}'.format(**FNC)
        mc.file(fileFormat, r=True, mnc=False)
        
        
    def loadTemp_onClicked(self):
        filePath = mc.fileDialog2(fileMode=1, caption="Load Template")      
        mc.file(filePath[0], i=True)
    
    # Rigging Functions Below
    # Rename locators
    def renameLoc(self, RNC):
        defLocators = mc.ls(sl=True, type='transform')
        for each in defLocators:
            checkNC = each.split('_')
            if checkNC[0] != '{locators}'.format(**RNC):
                '_'.join(checkNC)
                mc.rename(each, '{locators}_'.format(**RNC) + each)
            else:
                print(each)

    # Create Joints
    def createJoints(self, RNC):
        locators = mc.ls(sl=True, type='transform')
        for locator in locators:
            namingCon = locator.split('{locators}'.format(**RNC))
            print(namingCon[1])
            mc.select(cl=True)
            joint = mc.joint(n='{joints}'.format(**RNC) + namingCon[1])
            mc.delete(mc.parentConstraint(locator, joint))
            mc.delete(locator)
    
    # Classify Right, Left, and Middle Joints
    def classifyJoints(self, middleList, rightList, leftList):
        allJoints = mc.ls(type="joint")
        for eachJnt in allJoints:
            splitNames = eachJnt.split('_')
            if splitNames[1] == 'm':
                '_'.join(eachJnt)
                middleList.append(eachJnt)
            elif splitNames[1] == 'r':
                '_'.join(eachJnt)
                rightList.append(eachJnt)
            elif splitNames[1] == 'l':
                '_'.join(eachJnt)
                leftList.append(eachJnt)
            else:
                print('Nothing to classify')   

    def middleListParent(self, middleList):
        mc.select(middleList, r=True)
        midJoints = mc.ls(sl=True, type='joint')
        midNumber = len(midJoints)
        for mj in range(1, midNumber):
            mc.parent(midJoints[mj], midJoints[mj - 1])
    
    def leftListParent(self, leftList):
        mc.select(leftList, r=True)
        leftJoints = mc.ls(sl=True, type='joint')
        leftNumber = len(leftJoints)
        for lj in range(1, leftNumber):
            mc.parent(leftJoints[lj], leftJoints[lj - 1])
    
    def rightListParent(self, rightList):
        mc.select(rightList, r=True)
        rightJoints = mc.ls(sl=True, type='joint')
        rightNumber = len(rightJoints)
        for rj in range(1, rightNumber):
            mc.parent(rightJoints[rj], rightJoints[rj -1])
    
    def allParent(self, middleList, rightList, leftList):
        self.middleListParent(middleList)
        self.leftListParent(leftList)
        self.rightListParent(rightList)
    
        # Select all joints and freeze transforms
        allJoints = mc.ls(type="joint")
        mc.select(allJoints, r=True)
        mc.makeIdentity(a=True, r=True)
 
    # Create nurbs curve in the shape of cube
    def curve(self):
        curve = mel.eval('curve -d 1 -p -22.357529 22.357529 22.357529 -p -22.357529 -22.357529 22.357529 -p 22.357529 -22.357529 22.357529 -p 22.357529 22.357529 22.357529 -p -22.357529 22.357529 22.357529 -p -22.357529 22.357529 -22.357529 -p 22.357529 22.357529 -22.357529 -p 22.357529 22.357529 22.357529 -p 22.357529 -22.357529 22.357529 -p 22.357529 -22.357529 -22.357529 -p 22.357529 22.357529 -22.357529 -p 22.357529 -22.357529 -22.357529 -p -22.357529 -22.357529 -22.357529 -p -22.357529 22.357529 -22.357529 -p -22.357529 -22.357529 -22.357529 -p -22.357529 -22.357529 22.357529 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')
    
    # Creates a controller for each joint in their respective chains
    def createCtrls(self, RNC, middleList, rightList, leftList):
        allJoints = mc.ls(type='joint')
        mc.select(allJoints, r=True)
        midLast = middleList[len(middleList) - 1]
        mc.select(midLast, d=True)
        leftLast = leftList[len(leftList) - 1]
        mc.select(leftLast, d=True)
        rightLast = rightList[len(rightList) - 1]
        mc.select(rightLast, d=True)
        selJoints = mc.ls(sl=True, type='joint')
        print(selJoints)
        for i in range(len(selJoints)):
            self.curve()
            selCurve = mc.ls(sl=True, type='transform')[0]
            mc.delete(mc.parentConstraint(selJoints[i], selCurve))
            ctrlName = selJoints[i].replace('{joints}_'.format(**RNC), '{controllers}_'.format(**RNC))
            mc.rename(selCurve, ctrlName)
            print(ctrlName)     
        
my_widget = MyMayaWidget()     
my_widget.show()

