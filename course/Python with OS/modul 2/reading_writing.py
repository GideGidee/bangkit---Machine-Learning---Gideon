import os
import datetime

timestamp = os.path.getmtime("tes.txt")
print(datetime.datetime.fromtimestamp(timestamp))

dest_dir = os.path.join(os.getcwd(), "tes.txt")
print(dest_dir)