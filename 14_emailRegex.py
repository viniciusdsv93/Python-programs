# Program that searches for e-mails in a text sample and save them in a new text file.

import pyperclip, re, datetime

# paste the text sample from the clipboard.

textSample = pyperclip.paste()

# create a regex and use it on the sample.

emailRegex = re.compile(r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})')

moEmail = emailRegex.findall(textSample)

# create a .txt file and save the search results in it.

try:
    file = open('emails.txt', 'r')
    file.close()
except FileNotFoundError:
    file = open('emails.txt', 'w+')
    file.close()

with open('emails.txt', 'a') as file:
    file.write(str(f'{datetime.datetime.today()} E-mails founded {len(moEmail)}: {moEmail} \n'))
