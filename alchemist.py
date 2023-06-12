# pip install pyttsx3 - cmd to install python text to spech library
# pip install pypdf2 - for pdf files
import pyttsx3
from PyPDF2 import PdfFileReader
with open('the_alchemist.pdf', 'rb') as book:
# rb - read pdf as byte

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init() #initialization
    audio_reader.setProperty("rate", 150) #speed of reader

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()

        audio_reader.say(content)
        audio_reader.runAndWait()
