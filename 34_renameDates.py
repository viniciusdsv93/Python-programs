# Program that renames files with American to European date format.

import shutil, re, os

# create a regex to match files with the american date format.
datePattern = re.compile(r'''^(.*?) # text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                  # four digits for the year
    (.*?)$                          # text after the date
    ''', re.VERBOSE)

allFiles = os.listdir()

for amerFileName in allFiles:
    mo = datePattern.search(amerFileName)
    print(mo)
    # skip files without an american date format.
    if mo == None:
        continue

    # get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form the european filename.
    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    print(f'Renaming {amerFileName} to {euroFileName}.')
    shutil.move(amerFileName, euroFileName)
