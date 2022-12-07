import os
import maya.cmds as mc
import json
import maya.mel as mel

# Reference JSON File for rig Naming Convention

getRigNamingConvention = open(os.path.join(os.getcwd(), 'rigNamingConvention.json'))
RNC = json.load(getRigNamingConvention)

# Rename locators
def renameLoc():
    defLocators = mc.ls(sl=True, type='transform')
    for each in defLocators:
        checkNC = each.split('_')
        if checkNC[0] != '{locators}'.format(**RNC):
            '_'.join(checkNC)
            mc.rename(each, '{locators}_'.format(**RNC) + each)
        else:
            print(each)

renameLoc()

# Create Joints
def createJoints():
    locators = mc.ls(sl=True, type='transform')
    for locator in locators:
        namingCon = locator.split('{locators}'.format(**RNC))
        print(namingCon[1])
        mc.select(cl=True)
        joint = mc.joint(n='{joints}'.format(**RNC) + namingCon[1])
        mc.delete(mc.parentConstraint(locator, joint))
        mc.delete(locator)

createJoints()

# Joint Definitions and Lists
middleList = []
rightList = []
leftList = []

# Classify Right, Left, and Middle Joints
def classifyJoints():
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

    print(middleList)
    print(rightList)
    print(leftList)

if middleList != [] and leftList != [] and rightList != []:
    middleList = []
    leftList = []
    rightList = []
    classifyJoints()
elif middleList == [] and leftList == [] and rightList == []:
    classifyJoints()
else:
    print('Unable to classify joints')
def middleListParent():
    mc.select(middleList, r=True)
    midJoints = mc.ls(sl=True, type='joint')
    midNumber = len(midJoints)
    for mj in range(1, midNumber):
        mc.parent(midJoints[mj], midJoints[mj - 1])

def leftListParent():
    mc.select(leftList, r=True)
    leftJoints = mc.ls(sl=True, type='joint')
    leftNumber = len(leftJoints)
    for lj in range(1, leftNumber):
        mc.parent(leftJoints[lj], leftJoints[lj - 1])

def rightListParent():
    mc.select(rightList, r=True)
    rightJoints = mc.ls(sl=True, type='joint')
    rightNumber = len(rightJoints)
    for rj in range(1, rightNumber):
        mc.parent(rightJoints[rj], rightJoints[rj -1])

def allParent():
    middleListParent()
    leftListParent()
    rightListParent()

    # Select all joints and freeze transforms
    allJoints = mc.ls(type="joint")
    mc.select(allJoints, r=True)
    mc.makeIdentity(a=True, r=True)

allParent()

# Create nurbs curve in the shape of cube
def curve():
    curve = mel.eval('curve -d 1 -p -22.357529 22.357529 22.357529 -p -22.357529 -22.357529 22.357529 -p 22.357529 -22.357529 22.357529 -p 22.357529 22.357529 22.357529 -p -22.357529 22.357529 22.357529 -p -22.357529 22.357529 -22.357529 -p 22.357529 22.357529 -22.357529 -p 22.357529 22.357529 22.357529 -p 22.357529 -22.357529 22.357529 -p 22.357529 -22.357529 -22.357529 -p 22.357529 22.357529 -22.357529 -p 22.357529 -22.357529 -22.357529 -p -22.357529 -22.357529 -22.357529 -p -22.357529 22.357529 -22.357529 -p -22.357529 -22.357529 -22.357529 -p -22.357529 -22.357529 22.357529 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;')

# Creates a controller for each joint in their respective chains
def createCtrls():
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
        curve()
        selCurve = mc.ls(sl=True, type='transform')[0]
        mc.delete(mc.parentConstraint(selJoints[i], selCurve))
        ctrlName = selJoints[i].replace('{joints}_'.format(**RNC), '{controllers}_'.format(**RNC))
        mc.rename(selCurve, ctrlName)
        print(ctrlName)

createCtrls()

