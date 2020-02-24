import os
import shutil

if __name__ == '__main__':
    cwd = os.getcwd()+"\\"
    l = os.listdir(cwd)         #Listing Files in current working directory.
    for i in range(len(l)):

        if '.py' in l[i]:               #Searching for extension named as .py
            pyth = "Python Files\\"
            path = os.path.join(cwd,pyth)       #Naming a path for the python files to be moved.
            if "Python Files" not in os.listdir(cwd) and l[i]!="Gathered.py":
                os.mkdir(path)                  #creating a path using above named path for the python files to be moved.
                shutil.move(l[i],path)          #Moving python file if found.
            elif "Python Files" in os.listdir(cwd) and l[i]!="Gathered.py":
                shutil.move(l[i],path)          #Moving python file if found.

        elif any(s in l[i] for s in ('.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl')):          #Searching for extension realted to audio files.
            pyth = "Audio Files\\"
            path = os.path.join(cwd,pyth)       #Naming a path for the audio files to be moved.
            if "Audio Files" not in os.listdir(cwd):
                os.mkdir(path)                  #creating a path using above named path for the audio files to be moved.
                shutil.move(l[i],path)          #Moving audio file if found.
            elif "Audio Files" in os.listdir(cwd):
                shutil.move(l[i],path)          #Moving audio file if found.
