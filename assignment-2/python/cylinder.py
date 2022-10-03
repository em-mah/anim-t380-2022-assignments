import sys
import maya.cmds as cmds
import argparse
import maya.standalone
maya.standalone.initialize()

parser = argparse.ArgumentParser(description="This script creates a cylinder pyramid.")
parser.add_argument("num_cylinders", type=int, help="Number of cylinders")
parser.add_argument("radius_start", type=int, help="Starting radius")

args = parser.parse_args()

print("Creating {} cylinder(s)...".format(args.num_cylinders))

for i in range(args.num_cylinders):
    n = args.radius_start-(args.radius_start/args.num_cylinders)*i
    print("Created cylinder #{} with radius {}".format(i,n))
    cmds.polyCylinder(h=1, r=n)
    cmds.move(0,0.5+i,0)

print("Meshes in maya scene:")
print(maya.cmds.ls(geometry=True))

cmds.file (rename="C:/Users/emily/OneDrive/Documents/GitHub/anim-t380-2022-assignments/assignment-2/python/cylinder.ma")
cmds.file(save=True, type="mayaAscii")