# testing
import sys
import maya.cmds as cmds
import argparse
import maya.standalone
maya.standalone.initialize()

parser = argparse.ArgumentParser(description="This script creates a bunch of cylinders.")
parser.add_argument('num_cylinders', type=int, help="Number of cylinders")

args = parser.parse_args()

print("Creating {} cylinder(s)...".format(args.num_cylinders))

for i in range(args.num_cylinders):
    print("Created cylinder #{}".format(i))
    cmds.cylinder()

print("Meshes in maya scene:")
print(maya.cmds.ls(geometry=True))

cmds.file (rename="C:/Users/emily/OneDrive/Documents/GitHub/anim-t380-2022-assignments/assignment-2/python/test.ma")
cmds.file(save=True, type="mayaAscii")


