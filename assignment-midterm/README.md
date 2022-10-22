## **Midterm**
 
### **Description**
**Problem 2**
This script collects a sequence of frames and renames them in a configurable way, with the option to zip into an archive.
Extra feature: automatically generates a thumbnail and CSV including filename and date to be included in the zip archive.

### **Arguments**
This script takes the following arguments:
- `sequence_path` :   Type: str, path to sequence of frames for renaming
- `config_file` : Type: str, JSON file that stores client naming convention
- `zip` : Type: bool, option to zip into archive. 
- `-h, --help` :    Show this help message and exit

### **Example**
Run `python frame_rename.py [sequence_path] config.json True` in command prompt. It renames the sequence using the naming convention provided in config.json and creates a zip archive.