# Program of Mad Libs.

import re

# save a full text with the words ADJECTIVE, NOUN or VERB.

textSample = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

# ask the user to enter new words to replace them.

adjective = input('\nPlease, enter an adjective: \n')
noun = input('\nEnter a noun: \n')
verb = input('\nEnter a verb: \n')

# print the text with the correct replacements.

adjectiveRegex = re.compile(r'ADJECTIVE')
textSample = adjectiveRegex.sub(fr'{adjective}', textSample)

nounRegex = re.compile(r'NOUN')
textSample = nounRegex.sub(fr'{noun}', textSample)

verbRegex = re.compile(r'VERB')
textSample = verbRegex.sub(fr'{verb}', textSample)

print(textSample, '\n')

# save it to a text file.

with open('madLibs.txt', 'w') as file:
    file.write(textSample)
