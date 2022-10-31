import os, sys
import argparse
import json
from zipfile import ZipFile

parser = argparse.ArgumentParser(description="This script renames a file sequence.")
parser.add_argument("sequence_path", type=str, help="Path to sequence of frames for renaming")
parser.add_argument("-zip", action='store_true', help="Option to zip into archive")

args = parser.parse_args()

def getAssetMetadata():
    # Read naming convention config file
    metadata_file = open("naming_convention.json")
    return json.load(metadata_file)

metadata = getAssetMetadata()

save_file_format = "{shotname}.{task}.{artist}.{version}.{frame}.{ext}"

new_name = save_file_format.format(**metadata)

def increment(fileName):
    x = fileName.split(".")
    x[4] = str(int(x[4]) + 1).zfill(len(x[5])+1)
    newName = ".".join(x)
    return newName


print(args.sequence_path)
for i in os.listdir(args.sequence_path):
    os.rename(args.sequence_path+"/"+i, args.sequence_path+"/"+new_name)
    new_name = increment(new_name)
    print("incremented:", increment(new_name))

if args.zip == True:
    file_paths=[]
    for root, directories, files in os.walk(args.sequence_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    
    with ZipFile('renamed.zip','w') as zip:
        for file in file_paths:
            zip.write(file)