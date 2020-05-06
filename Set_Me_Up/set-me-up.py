import os

print('''Modes of operation: 
\n1. Manual Mode - A mode where the user provides all the names of folders and sub-folders.
\n2. Automatic Mode - A mode where only the name (with complete location) of the text file is 
given which contains a list of names for the folders and the parent folder is named after the name of the text file\n''')

mode=int(input("Enter Mode: "))

if mode==1:
    print('''STEPS:
    \n1. Choose the location to make directories and/or sub-directories.
    \n2. Enter the name of the parent directory.
    \n3. Enter the number of sub-directories to be created
    \n4. Give the name to the corresponding sub-directories.''')
    path = input("Enter Location (provide full path) \n: ")
    if path.lower()=='this':
        path=os.getcwd()
    path = path.replace("/", "\\")
    if os.path.exists(path):
        os.chdir(path)
        name = input("Enter name of parent directory:  ")
        os.mkdir(path+"\\"+name)
        folder = int(input("How my folders? \n: "))
        for i in range(folder):
            os.mkdir(path+"\\"+name+"\\"+input("Folder " + str(i+1) + " name: "))
    else:
        print("No such path exists. Provide correct path")
    print("Task completed successfully")

elif mode==2:
    print("File(s) : " ,[i for i in os.listdir() if os.path.isfile(i)==True])
    file=input("Enter file: ")
    file_=file[0:-4]+"\\"
    with open(file,'r') as f:
        if os.path.exists(file_)==False:
            os.mkdir(file_)
        for i in f.readlines():
            if '\n' in i:
                i=i[0:-1]
            i=i.replace(":"," -")
            os.mkdir(file_+i)
    print("Task completed successfully")
else:
    print("Error: Wrong option provided")
    
