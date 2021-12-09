# Program that search for files with 10MB or more in a specific folder and print their paths on the screen.

import os, send2trash

# walk through subfolders and files inside a specific folder.

for folderName, subFolders, fileNames in os.walk('C:\\users\\Vinícius\\Desktop\\test'):
    for fileName in fileNames:
        path = os.path.join(folderName, fileName)
        size = os.path.getsize(path)
        if size > 1000000:
            print(f'\nThe file {fileName} has {size} bytes\n')
            print(f'It\'s path is: {path}.')
            delAnswer = input('\nDo you want to delete it? [Y/N] ').strip().upper()[0]
            if delAnswer == 'Y':
                send2trash.send2trash(path)
                input('\nFile sent to recycle bin successfully.')
            else:
                continue

print()

# look for files with 10MB or more.

# print their path.