import os
from PIL import Image

def make_pdf_from_images(storage_path, imglist):
    imagelist=[]
    for i in imglist:
        img= (Image.open(i)).convert('RGB')
        img = img.resize((round(img.width*0.90), round(img.height*0.90)), resample=Image.LANCZOS)
        imagelist.append(img)
    pdfpath=storage_path+"Image_to_pdf.pdf"
    img= (Image.open(imglist[0])).convert('RGB')
    img = img.resize((round(img.width*0.90), round(img.height*0.90)), resample=Image.LANCZOS)
    img.save(pdfpath, resolution=70.0 , save_all=True, append_images=imagelist[1::])
    print(f"Done combining {len(imagelist)} images to a PDF !!")

print("Only Supports PNG, JPEG and JPG files \nCurrent Directory List: ", os.listdir())

imglist = [i for i in os.listdir() if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg")]

if len(imglist) != 0:
    storage_path = "Image_To_PDF/"
    if os.path.exists(storage_path) == False:
        os.mkdir(storage_path)
    make_pdf_from_images(storage_path, imglist)
else:
    print("No Supported format found")