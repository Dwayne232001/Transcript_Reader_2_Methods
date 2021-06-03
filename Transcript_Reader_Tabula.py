import csv
import tabula
file = "Sample_Transcript_1.pdf"
tables = tabula.read_pdf(file,pages=1,multiple_tables=True)
x=0
"""To convert into a text file"""
try: 
    with open("Transcript2.txt", "a", newline="") as file:
        while x<8:
            file.write(str(tables[x]))
            x=x+1
except OSError: 
    print('Failed creating the file') 
else: 
    print('File created')
"""To convert into a csv file""" 
# tabula.convert_into(file, "Transcript.csv", output_format="csv", pages='all')
