import os
from PIL import Image
print("Only Supports PNG, JPEG and JPG files \nCurrent Directory: ", os.listdir())
tmp = []
imagelist = [i for i in os.listdir() if i.endswith(
    ".png") or i.endswith(".jpg") or i.endswith(".jpeg")]
print(imagelist)
if len(imagelist) != 0:
    for i in imagelist[1::]:
        img = Image.open(i, 'r')
        tmp.append(img)
    img = Image.open(imagelist[0], 'r')
    img.save('ALL_IMAGE_PDF.pdf', save_all=True, append_images=tmp)
    print(f"Done combining {len(imagelist)} images to a PDF !!")
else:
    print("No Supported format found")
