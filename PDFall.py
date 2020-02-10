from PIL import Image
import os

if __name__ == '__main__':
    cwd = os.getcwd()
    l = os.listdir(cwd)
    img_list = []
    imagelist = []
    for i in l:
        if '.' in i and len(i)>=6:
            if i[-5] == '.' and i[-4:] == 'jpeg':
                img_list.append(i)
            elif i[-4] == '.' and (i[-3:] == 'jpg' or i[-3:] == 'png'):
                img_list.append(i)
    for i in img_list:
        image1 = Image.open(cwd+'\\'+i,"r")
        im1 = image1.convert('RGB')
        imagelist.append(im1)
    im1.save(cwd+'\myImages.pdf',save_all=True, append_images=imagelist)
