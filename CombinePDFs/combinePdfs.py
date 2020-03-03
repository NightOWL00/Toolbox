import PyPDF2, os
directory=''
pdfFiles = []
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
