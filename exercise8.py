"""
Write a program to manipulate pdf files using pypdf. Your programs should be able to
merge multiple pdf files into a single pdf. You are welcome to add more functionalities.

"""
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files =  [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merger-pdf.pdf")
merger.close()
