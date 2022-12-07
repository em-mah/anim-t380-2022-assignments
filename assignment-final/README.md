## **Final Assignment**

Erika Taylor & Emily Mah

### **Description**
This script aids the prop-rigging process by creating a simple procedural rig based on locator placement.

### **Process**
- Press Reference Model
- Create and place locators on the model (or press Load Template as needed)
- Select all Locators
- Press Build Rig

### **Example**
Run `procedural-rig.py` in Maya script editor. It can also be saved to the Maya shelf. A UI will open and provide the following buttons:
 - `Reference Model` opens a file dialog where user can select the model they want to reference.
 - `Load Template` opens a file dialog where user can import any existing locator templates.
 - `Build Rig` automatically builds a simple rig/joint hierarchy based on locator placement. It renames the locators, creates and parents joints, and creates basic controllers during this process.
 - `Reload Version` selects a version of the referenced model based on a naming convention and replaces current reference with selected.

### Notes:
Additional features - would like to continue developing features for tool (ie. build rig without empty spaces between joints)
Naming conventions stored in JSON file in etc folder