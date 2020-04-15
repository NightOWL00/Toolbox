import random
import string


def make_names(file_names):
    tmp = []
    files = ['.docx', '.pdf', '.txt', '.abc',
             '.pptx', '.exe', '.jpg', '.jpeg', '.png']
    for i in file_names:
        i = i+random.choice(files)
        tmp.append(i)
    return tmp


alpha = string.ascii_letters
number = int(input('Enter number of files to be created: '))
f = ''
file_names = []
for j in range(number):
    for i in range(13):
        x = random.randint(0, len(alpha)-1)
        f = f+alpha[x]
    file_names.append(f)
    f = ''

file_names = make_names(file_names)
