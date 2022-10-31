## **Midterm**
 
### **Description**
**Problem 2**
This script collects a sequence of frames and renames them in a configurable way, with the option to zip into an archive.

### **Arguments**
This script takes the following arguments:
- `sequence_path` :   Type: str, path to sequence of frames for renaming
- `-zip` : Type: bool, option to zip into archive. 
- `-h, --help` :    Show this help message and exit

### **Example**
Run `python frame_rename.py [sequence_path] -zip` in command prompt. It renames the sequence using the naming convention provided in config.json and creates a zip archive.