import glob, os
from PyPDF2 import PdfFileMerger

input_paths = glob.glob('D:/Keep/Resume/to_merge/input/*.pdf')

merger = PdfFileMerger()

for path in input_paths:
    merger.append(open(path,'rb'))

with open('D:/Keep/Resume/to_merge/output/joined.pdf', 'wb') as arg:
    merger.write(arg)
