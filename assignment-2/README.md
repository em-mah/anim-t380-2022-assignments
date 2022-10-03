## **Assignment 2**
 
### **Description**
This script creates a cylinder pyramid.

### **Arguments**
- `num_cylinders` :   Type: int, number of cylinders
- `radius_start` : Type: int, starting radius
- `-h, --help` :    Show this help message and exit

### **Example**
Run  `mayapy cylinder.py 4 2` in command prompt. It should print out the following:

    Creating 4 cylinder(s)...
    Created cylinder #0 with radius 2.0
    Created cylinder #1 with radius 1.5
    Created cylinder #2 with radius 1.0
    Created cylinder #3 with radius 0.5
    Meshes in maya scene:
    ['pCylinderShape1', 'pCylinderShape2', 'pCylinderShape3', 'pCylinderShape4']
4 stacked cylinders will be created in a maya scene and saved in a file called `cylinder.ma`.