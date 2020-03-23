import tkinter as tk


def add():
    pass


def sub():
    pass


def div():
    pass


def mul():
    pass


window = tk.Tk()
window.geometry('450x200')
window.resizable(0, 0)
window.iconbitmap('cal.ico')
# 2 labels
num1Label = tk.Label(window, text=' Number 1: ')
num1Label.grid(row=0, column=0)
num2Label = tk.Label(window, text=' Number 2: ')
num2Label.grid(row=0, column=2)
# 2 input
num1 = tk.Entry(window)
num1.grid(row=0, column=1)
num2 = tk.Entry(window)
num2.grid(row=0, column=3)
# 4 button
addbtn = tk.Button(window, text=' ADD ')
subbtn = tk.Button(window, text=' SUB ')
divbtn = tk.Button(window, text=' DIV ')
mulbtn = tk.Button(window, text=' MUL ')
addbtn.grid(row=1, column=0)
subbtn.grid(row=1, column=1)
divbtn.grid(row=1, column=2)
mulbtn.grid(row=1, column=3)

window.mainloop()
