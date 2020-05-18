from huepy import *
import pyscreenshot as ImageGrab
from pynput.mouse import Button, Controller
import time
import os
import sys
from PIL import Image


def check_for_errors(dimentions, pages):
    if len(dimentions) != 4:
        return False
    if pages <= 0:
        return False
    for _ in dimentions:
        if _ < 0:
            return False


def make_pdf_from_images(storage_path, pages):
    imagelist = []
    for i in range(1, pages):
        img = Image.open(storage_path + str(i) + '.png')
        img1 = img.convert('RGB')
        imagelist.append(img1)
    pdfpath = storage_path+"ss2pdf.pdf"
    img2 = Image.open(storage_path+'0.png').convert('RGB')
    img2.save(pdfpath, save_all=True, append_images=imagelist)

    print(good(lightgreen("Successfully converted to pdf")))


print(info(bold(yellow('''This program will capture screenshots and then convert it to PDF.
                       After running this program screenshots will be taken after 2 seconds.
                       Do not move the pointer until the process is completed.'''))))
mouse = Controller()
storage_path = 'SS2PDF_folder'  # Change name from here
if os.path.exists(storage_path) == False:
    os.mkdir(storage_path)
    print(info(f"path created : {storage_path}"))
if storage_path[-1] != "/":
    storage_path = storage_path+"/"

pages = int(input(que("Enter the no of screenshots to be taken: ")))
dimentions = tuple(
    map(int, input(que("Enter dimentions (FORMAT: X1,Y1,X2,Y2) : ")).split(" ")))
mouse.position = (960, 540)

if check_for_errors(dimentions, pages) == False:
    print("Invalid input from user.")
    sys.exit

for i in range(10):
    os.system('cls')
    print("Place mouse pointer to the location where you want it to click. And click on that window to hide this CMD window")
    print(f"You have {10-i} seconds to move the cursor to the position.")
    time.sleep(1.05)
os.system('cls')
print("Capturing screenshots right now....")

for i in range(pages):
    time.sleep(0.05)
    im = ImageGrab.grab(bbox=dimentions)
    mouse.click(Button.left, 1)
    im.save(storage_path + str(i) + '.png')

print(good("Done with capturing screenshots."))
make_pdf_from_images(storage_path, pages)
input(green(bold("Press ENTER to exit")))
