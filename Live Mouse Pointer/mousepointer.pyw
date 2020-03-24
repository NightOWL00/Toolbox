import pyautogui
import tkinter as tk
import time


def magic():
    pos = pyautogui.position()
    lb1['text'] = str(pos)


def Refresher():
    magic()
    window.after(50, Refresher)


window = tk.Tk()
window.iconbitmap('cursor.ico')
window.geometry('205x35')
window.wm_attributes("-topmost", 1) # so that windows stays at top
window.title('MPOS')
window.resizable(0, 0)
lb1 = tk.Label(window, text='  ')
lb1.grid(column=0, row=0, padx=(5, 0), pady=(3, 3), ipadx=(3), ipady=(1))
Refresher()
window.mainloop()
