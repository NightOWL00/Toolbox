from huepy import *
import pyscreenshot as ImageGrab
from pynput.mouse import Button, Controller
import time
import os
import sys
from PIL import Image


def makepdf(storage_path, pages):
    imagelist = []
    img = Image.open(storage_path + "0.png")
    for i in range(1, pages):
        img1 = Image.open(storage_path + str(i) + '.png')
        img1.convert('RGB')
        imagelist.append(img1)
    pdfpath = storage_path+"book.pdf"
    img.save(pdfpath, save_all=True, append_images=imagelist)
    print(good(lightgreen("Successfully converted to pdf")))


print(info(bold(yellow("This program will capture screenshots and then convert it to PDF\nAfter running this program screenshots will be taken after 2 seconds\nDo not move the pointer until the process is completed."))))
try:
    mouse = Controller()
    storage_path = input(que("Enter Storage path (Default: Current working directory) : "))
    if os.path.exists(storage_path):
        print(info(f"path is : {storage_path}"))
    else:
        os.mkdir(storage_path)
        print(info(f"path created : {storage_path}"))
    pages = int(input(que("Enter the no of screenshots to be taken: ")))
    dimentions = tuple(
        map(int, input(que("Enter dimentions (FORMAT: X1,Y1,X2,Y2) : ")).split(" ")))
    mouse_pointer_position = tuple(map(int, input(
        que("Enter mouse pointer position (where to click) : ")).split(" ")))

    if len(dimentions) != 4:
        print(bad(red("DIMESIONS are WRONG!!")))
        sys.exit
    if len(mouse_pointer_position) != 2:
        print(bad(red("Mouse pointer error")))
        sys.exit
    if storage_path[-1] != "/":
        storage_path = storage_path+"/"
    mouse.position = mouse_pointer_position

    time.sleep(3)
    for i in range(pages):
        time.sleep(0.05)
        im = ImageGrab.grab(bbox=dimentions)
        mouse.click(Button.left, 1)
        im.save(storage_path + str(i) + '.png')

    print(good("Done with capturing screenshots."))
    makepdf(storage_path, pages)
except Exception as e:
    print(bad(red("Some error occured")))
finally:
    input(green(bold("Press ENTER to exit")))
