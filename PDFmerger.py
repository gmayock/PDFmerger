import glob, os
from PyPDF2 import PdfFileMerger

input_paths = glob.glob('filepath/input/*.pdf')

merger = PdfFileMerger()

for path in input_paths:
    merger.append(open(path,'rb'))

with open('filepath/output/merged.pdf', 'wb') as arg:
    merger.write(arg)
