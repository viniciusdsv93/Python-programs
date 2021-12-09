# Program that searches for a specific type of file and automatically delete them.

import os, re, send2trash

# list all the files in a folder.

os.chdir('C:\\Users\\Vinícius\\Desktop\\test')

allFiles = os.listdir()

# create a regex with the type of file that needs to be deleted.

delFileRegex = re.compile(r'(.*).txt')

# search for files with that extension in the selected folder.

totalFilesDeleted = 0

print('\nProcessing...\n')

for fileSample in allFiles:
    mo = delFileRegex.search(fileSample)

    if mo == None:
        continue

    # send the correct files to the recycle bin.

    send2trash.send2trash(str(mo.group()))
    totalFilesDeleted += 1

# print the total number of files deleted.

print(f'\nIn total, {totalFilesDeleted} files were sent to the recycle bin.\n')
