import os

x=[i for i in os.listdir() if i[-3::]==".py"]
x.remove("Auto-Login-Maker.py")
x.remove("loginALL.py")

for i in x:
    os.system(f"python {i}")