import tkinter as tk


def add():
    x = int(num1.get())
    y = int(num2.get())
    oplbl['text'] = str(x+y)


def sub():
    x = int(num1.get())
    y = int(num2.get())
    oplbl['text'] = str(x-y)


def div():
    x = int(num1.get())
    y = int(num2.get())
    oplbl['text'] = str(x/y)


def mul():
    x = int(num1.get())
    y = int(num2.get())
    oplbl['text'] = str(x*y)


window = tk.Tk()
window.title("Advance Calculator")
window.geometry('460x180')
window.resizable(0, 0)
window.iconbitmap('cal.ico')
# 2 labels
num1Label = tk.Label(window, text=' Number 1: ')
num1Label.grid(row=0, column=0, padx=5, pady=5, ipadx=3, ipady=3)
num2Label = tk.Label(window, text=' Number 2: ')
num2Label.grid(row=0, column=2, padx=5, pady=5, ipadx=3, ipady=3)
# 2 input
num1 = tk.Entry(window)
num1.grid(row=0, column=1, padx=5, pady=5, ipadx=3, ipady=3)
num2 = tk.Entry(window)
num2.grid(row=0, column=3, padx=5, pady=5, ipadx=3, ipady=3)
# 4 button
addbtn = tk.Button(window, text=' ADD ', command=add)
subbtn = tk.Button(window, text=' SUB ', command=sub)
divbtn = tk.Button(window, text=' DIV ', command=div)
mulbtn = tk.Button(window, text=' MUL ', command=mul)
addbtn.grid(row=1, column=0, padx=5, pady=5, ipadx=3, ipady=3)
subbtn.grid(row=1, column=1, padx=5, pady=5, ipadx=3, ipady=3)
divbtn.grid(row=1, column=2, padx=5, pady=5, ipadx=3, ipady=3)
mulbtn.grid(row=1, column=3, padx=5, pady=5, ipadx=3, ipady=3)
# output label
oplbl = tk.Label(window, text=' ')
oplbl.grid(row=2, column=0, columnspan=4, padx=5, pady=5, ipadx=3, ipady=3)
window.mainloop()
