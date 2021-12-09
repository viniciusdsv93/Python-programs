from time import sleep
import os

database = open('database.txt', 'r+')

username = input('Username: ').lower()

list = []

for l in database:
    list.append(l)


if username in list:
    print('in use')
else:
    database.write(f'{username}\n')
    print('ok')

print(list)