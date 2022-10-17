import os
import sys
import maya.cmds as cmds
import argparse
import maya.standalone
maya.standalone.initialize()

parser = argparse.ArgumentParser(description="This script creates an empty group with asset name.")
parser.add_argument("asset_name", type=str, help="Asset name")
parser.add_argument("output", type=str, help="output")

args = parser.parse_args()

cmds.group(em=True,name = args.asset_name)

savePath = os.getcwd()
saveFile = savePath + args.output
cmds.file (rename=saveFile)
cmds.file(save=True, type="mayaAscii")
