import os

def magic(path):
    os.chdir(path)
    name = input("Enter name of parent directory:  ")
    os.mkdir(path+"\\"+name)
    folder = int(input("How my folders? \n: "))
    for i in range(folder):
        os.mkdir(path+"\\"+name+"\\"+input("Folder " + str(i+1) + " name: "))


print("STEPS: \n1. Choose the location to make directories and/or sub-directories.\n2. Enter the name of the parent directory.\n3. Enter the number of sub-directories to be created\n4. Give the name to the corresponding sub-directories.")
path = input("Enter Location (provide full path) \n: ")
path = path.replace("/", "\\")
if os.path.exists(path):
    magic(path)
else:
    print("No such path exists")
print("Task completed successfully")
