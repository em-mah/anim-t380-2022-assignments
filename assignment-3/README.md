## **Assignment 3**
 
### **Description**
`.aliases` sets an environment variable named `asset`.
`env-mkdir.sh` uses above environment variable to make directory `assets/$asset/maya/scenes`. Runs `prep_asset.py` and places Maya file in said directory.
`prep_asset.py` creates an empty group in Maya using asset name. 

### **Arguments**
- `asset_name` :    Asset name
- `-h, --help` :    Show this help message and exit

### **Example**
Run  `bin/env-mkdir.sh` in bash command prompt. A new directory `./asset/$asset/maya/scenes` is created with a new Maya scene called `assignment_3.ma`. In it is an empty group with asset name.