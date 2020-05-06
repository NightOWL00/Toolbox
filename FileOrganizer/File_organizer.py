import os
import shutil

# Removing Folders
files=[]
for i in os.listdir():
    if os.path.isfile(i)==True:
        files.append(i)

# Removing main file name
files.remove('File_organizer.py')

# Getting Extensions and files
fn_ext=[i.split(".") for i in files]

# Creating folders and moving
for i in range(len(fn_ext)):
    if os.path.exists(fn_ext[i][1]+"__files")==False:
        os.mkdir(fn_ext[i][1]+"__files")
        shutil.move(files[i],fn_ext[i][1]+"__files")
    else:
        shutil.move(files[i],fn_ext[i][1]+"__files")

print("DONE")
