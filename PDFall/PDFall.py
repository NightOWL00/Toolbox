from PIL import Image
import os

if __name__ == '__main__':

    cwd = os.getcwd()  # For Getting Current Working Directory.
    l = os.listdir(cwd)  # Making List of FILES in corresponding Directory.
    img_list = []
    imagelist = []
    # Loop to find FILES of images format and making a list of them.
    for i in l:
        if '.' in i and len(i) >= 6:
            if i[-5] == '.' and i[-4:] == 'jpeg':
                img_list.append(i)
            elif i[-4] == '.' and (i[-3:] == 'jpg' or i[-3:] == 'png'):
                img_list.append(i)
    # Loop to convert Images into a PDF file.
    for i in img_list:
        image1 = Image.open(cwd+'\\'+i, "r")
        im1 = image1.convert('RGB')
        imagelist.append(im1)
    image1 = Image.open(cwd+'\\'+img_list[0], "r")
    # To save the PDF file.
    imagelist = imagelist[1::]
    image1.save(cwd+'\ALL_IMAGE_PDF.pdf',
                save_all=True, append_images=imagelist)
