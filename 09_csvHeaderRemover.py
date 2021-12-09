# Program that removes the header of several CSV files

import csv, os

allFiles = os.listdir()
csvFiles = []

for f in allFiles:
    if f.endswith('.csv'):
        csvFiles.append(f)

for f in csvFiles:
    print('Removing header from ' + f)
    csvRows = []    
    csvFile = open(f)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue # skip the first row, where the header is
        else:
            csvRows.append(row)
    csvFile.close()
    print('Saving new file of ' + f + '\n')
    newCsvFile = open(f'new{f}', 'w', newline = '')
    csvWriter = csv.writer(newCsvFile)
    for row in csvRows:
        csvWriter.writerow(row)
    newCsvFile.close()
