# Malin Yamato 
# Program to strip all the blanks off the start and ending of fiels and folders
# 
# Usge:    stripper.py <location of your files>
#

import os
import sys

folder = sys.argv[1]

def strip_folder(base):

    for file_name in os.listdir(base):

        print(file_name)
        source = base + file_name
        new_filename = file_name.strip()
        destination = base + new_filename
        os.rename(source, destination)
    
        if os.path.isdir(os.path.join(base, new_filename)):
            strip_folder(base + new_filename + '/')
    
    res = os.listdir(folder)
    print(res)

strip_folder(folder)

print('Done, all files stripped')


