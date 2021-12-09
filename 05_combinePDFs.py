# Program that combine only the selected pages of several pdf files

import PyPDF2, os

pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

for file in pdfFiles:
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfFileObj.close()

resultPdf = open('resultPdf.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
