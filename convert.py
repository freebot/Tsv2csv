import csv

# read tab-delimited file
with open('Reporte+de+listados+activos+10-26-2020.txt','r', encoding="latin-1") as fin:
    cr = csv.reader(fin, delimiter='\t')
    filecontents = [line for line in cr]

# write comma-delimited file (comma is the default delimiter)
with open('Stock.csv','w') as fou:
    cw = csv.writer(fou, quotechar='', quoting=csv.QUOTE_NONE, escapechar='\\')
    cw.writerows(filecontents)
