import os, sys
import maya.cmds as cmds


fileName = cmds.file(q=True, sn=True, shn=True)

x = fileName.split(".")
x[3] = str(int(x[3]) + 1)
newName = ".".join(x)

filePath = cmds.file(q=True, sn=True)

saveFile = filePath.replace(fileName, newName)
cmds.file(rename=saveFile)
cmds.file(save=True, type="mayaAscii")
