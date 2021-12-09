# Program that copies a .pdf file and rotates its pages, creating a new file

import PyPDF2

pdfFile1 = open('DECISION.pdf', 'rb')
pdfFile1Reader = PyPDF2.PdfFileReader(pdfFile1)
pdfFile2 = open('DECISION2.pdf', 'wb')

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfFile1Reader.numPages):
    pageObj = pdfFile1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    pdfWriter.write(pdfFile2)

pdfFile2.close()
pdfFile1.close()

pdfRotateObj = open('DECISION2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfRotateObj)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    page.rotateClockwise(90)
    pdfWriter.addPage(page)
resultPdfFile = open('DECISION_ROTATE.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
pdfRotateObj.close()
