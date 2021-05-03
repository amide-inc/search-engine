import urllib.request
import PyPDF2
response = urllib.request.urlopen(
    "https://nlp.stanford.edu/IR-book/pdf/01bool.pdf")
file = open("test.pdf", 'wb')
file.write(response.read())
pdfFileObj = open('test.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)
