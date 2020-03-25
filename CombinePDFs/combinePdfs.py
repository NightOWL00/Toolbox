from PyPDF2 import PdfFileMerger
import os
print('''Modes of Operation:
1: To combine all the PDFs in the directory enter 'a'.
2: To combine some of PDFs in the folder enter 's'.
''')
pdfs_in_dir = [i for i in os.listdir() if i.endswith(".pdf")]
print("List of PDFs: ", pdfs_in_dir)
merger = PdfFileMerger()
mode = input('Enter mode: ')

if mode == 'a':
    for pdf in pdfs_in_dir:
        merger.append(pdf)

if mode == 's':
    specific_pdf_list = []
    numpdf = int(input("Number of pdfs to combine: "))
    while numpdf > 0:
        name = input(f"Enter name of PDF at position {numpdf}: ")
        specific_pdf_list.append(name)
        numpdf -= 1
    specific_pdf_list = specific_pdf_list[::-1]
    for pdf in specific_pdf_list:
        merger.append(pdf)
merger.write("Combined.pdf")
merger.close()
