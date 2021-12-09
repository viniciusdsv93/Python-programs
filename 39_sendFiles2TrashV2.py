# Program that searches for a specific type of file and automatically delete them.

import os, re, send2trash

# list all the files in a folder.

os.chdir('C:\\Users\\Vinícius\\Desktop\\test')

allFiles = os.listdir()

# create a regex with the type of file that needs to be deleted.

delTxtRegex = re.compile(r'(.*).txt')
delOdsRegex = re.compile(r'(.*).ods')
delZipRegex = re.compile(r'(.*).zip')
delOdpRegex = re.compile(r'(.*).odp')

# search for files with that extension in the selected folder.

answer = str(input('''\nWich type of file do you want do delete?
[1] .txt
[2] .ods
[3] .zip
[4] .odp\n'''))

totalFilesDeleted = 0

print('\nProcessing...\n')

if answer == '1':
    option = '.txt'
    for fileSample in allFiles:
        mo = delTxtRegex.search(fileSample)

        if mo == None:
            continue

        # send the correct files to the recycle bin.

        send2trash.send2trash(str(mo.group()))
        totalFilesDeleted += 1

if answer == '2':
    option = '.ods'
    for fileSample in allFiles:
        mo = delOdsRegex.search(fileSample)

        if mo == None:
            continue

        # send the correct files to the recycle bin.

        send2trash.send2trash(str(mo.group()))
        totalFilesDeleted += 1

if answer == '3':
    option = '.zip'
    for fileSample in allFiles:
        mo = delZipRegex.search(fileSample)

        if mo == None:
            continue

        # send the correct files to the recycle bin.

        send2trash.send2trash(str(mo.group()))
        totalFilesDeleted += 1

if answer == '4':
    option = '.odp'
    for fileSample in allFiles:
        mo = delOdpRegex.search(fileSample)

        if mo == None:
            continue

        # send the correct files to the recycle bin.

        send2trash.send2trash(str(mo.group()))
        totalFilesDeleted += 1

# print the total number of files deleted.

print(f'\nIn total, {totalFilesDeleted} {option} files were sent to the recycle bin.\n')
