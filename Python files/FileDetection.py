# - - -   FILE DETECTION - - - 

import os

path = "C:\\Users\\Onur\\Desktop\\FOLDER"

if os.path.exists(path):
    print("that location is exists") 
    if os.path.isfile(path):
        print("that is a file!")
    elif os.path.isdir(path):
        print("that is a folder path!")
else:
    print("this location doesnt exists")








