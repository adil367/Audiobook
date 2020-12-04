import PyPDF2 as pp
import pyttsx3
#Taking pdf path as input
pdf=input("Enter the path of your pdf:\n")
book=open(pdf,'rb')
pdfreader= pp.PdfFileReader(book)
# getting the number of pages in the pdf
pages=pdfreader.numPages
print(f"There are {pages} number of pages in your pdf")
reader=pyttsx3.init()
# getting the voice available in the system
voices=reader.getProperty("voices")
# setting the voice of the reader
reader.setProperty("voice",voices[1].id)
for num in range(pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    reader.say(text)
    reader.runAndWait()


