import sys
import subprocess
import os

file = sys.argv[1]

with open(file, 'r') as f:
    files = f.readlines()

data_dir = "../data/"

for old_file in files:
    old_file = old_file.strip()

    new_file = old_file.replace('tes', 'halo')

    old_file_fullpath = os.path.join(data_dir, os.path.basename(old_file))
    new_file_fullpath = os.path.join(data_dir, os.path.basename(new_file))

    try:
        subprocess.run(['mv', old_file_fullpath, new_file_fullpath])
    except subprocess.CalledProcessError as e:
        print(f"Error renaming {old_file_fullpath}: {e}")
    except FileNotFoundError:
        print(f"File {old_file_fullpath} not found.")
