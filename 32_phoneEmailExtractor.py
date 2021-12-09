# Program that extracts phone numbers and emails from the clipboard.

import pyperclip, re

# paste the text from the clipboard.

textSearch = str(pyperclip.paste())

# create two regexes to find phone numbers and emails in it.

phoneNumRegex = re.compile(r'(\d\d\d\d\d-\d\d\d\d)')

moPhone = phoneNumRegex.findall(textSearch)

emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.\w+)')

moEmail = emailRegex.findall(textSearch)

# create a new string with the data founded.

moFinal = moPhone + moEmail

# paste it on the clipboard.

if moFinal == []:
    print('No matches.')
else:
    print(moFinal)
    pyperclip.copy(str(moFinal))
    