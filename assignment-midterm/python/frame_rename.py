import os, sys
import argparse

parser = argparse.ArgumentParser(description="This script renames a file sequence.")
parser.add_argument("sequence_path", type=str, help="Path to sequence of frames for renaming")
parser.add_argument("config_file", type=str, help="JSON file that stores client naming convention")
parser.add_argument("zip", type=bool, help="Option to zip into archive")

args = parser.parse_args()

print(args.sequence_path, args.config_file, args.zip)