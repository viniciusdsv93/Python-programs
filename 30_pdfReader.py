# Program to read text from a .pdf file

import PyPDF2

pdfFileObj = open('DECISION.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
textSample = pageObj.extractText()
print(textSample)
with open('textPDF.txt', 'w') as file:
    file.write(textSample)
    print('Text file successfully created.')
print(pdfReader.isEncrypted)
pdfFileObj.close()

