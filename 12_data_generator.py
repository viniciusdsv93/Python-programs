from os import system
from time import sleep
from random import choice

try:
    file = open('database2.txt', 'r')
    file.close()
except FileNotFoundError:
    file = open('database2.txt', 'a')
    file.close()

while True:
    print('=' * 50)
    print('DATA GENERATOR'.center(50))
    print('=' * 50)
    print("""Select one of the following options:

[1] - Show data list_name
[2] - Generate new data
[3] - Exit program
""")
    print('=' * 50)
    print()
    while True:
        option = str(input('Your option: '))
        if option in "1 2 3":
            break
        print('Error. Please, enter a valid option')

    if option == '3':
        print()
        print('Closing program...')
        print()
        sleep(1)
        break

    if option == '1':
        system('cls')
        print()
        print('=' * 50)
        print('DATA LIST'.center(50))
        print('=' * 50)
        file = open('database2.txt', 'r')
        for line in file:
            print(line)
        print()
        input('Press anything to continue.')
        system('cls')
    
    if option == '2':
        system('cls')
        print()
        print('=' * 50)
        print('GENERATE NEW DATA'.center(50))
        print('=' * 50)
        print("""Select one of the following data classes to create:
        
[1] - Name
[2] - Email
[3] - Cel phone
[4] - City
[5] - State
""")
        print('=' * 50)
        print()
        while True:
            secondary_option = str(input('Your option: '))
            if secondary_option in "1 2 3 4 5":
                break
            print('Error. Please, enter a valid option')
        
        if secondary_option == '1':
            list_name = ['Maria', 'Bianca', 'Marcos', 'Andrea', 'Fernanda']
            result = choice(list_name)
            file = open('database2.txt', 'a', encoding = 'utf-8')
            file.write(f'{result}\n')
            print()
            print(f'Data {result} inserted on the file with success.')
            file.close()
        
        elif secondary_option == '2':
            list_email = ['maria@gmail.com', 'bianca@yahoo.com', 'marcos@outlook.com', 'andrea@gmail.com', 'fernanda@fernanda.com']
            result = choice(list_email)
            file = open('database2.txt', 'a', encoding = 'utf-8')
            file.write(f'{result}\n')
            print()
            print(f'Data {result} inserted on the file with success.')
            file.close()

        elif secondary_option == '3':
            list_cel_phone = ['9 8526-7854', '9 8789-5256', '9 9869-7741', '9 8547-4112', '9 8563-9968']
            result = choice(list_cel_phone)
            file = open('database2.txt', 'a', encoding = 'utf-8')
            file.write(f'{result}\n')
            print()
            print(f'Data {result} inserted on the file with success.')
            file.close()

        elif secondary_option == '4':
            list_city = ['Sao Paulo', 'Belo Horizonte', 'Manaus', 'Avare', 'Florianopolis']
            result = choice(list_city)
            file = open('database2.txt', 'a', encoding = 'utf-8')
            file.write(f'{result}\n')
            print()
            print(f'Data {result} inserted on the file with success.')
            file.close()

        elif secondary_option == '5':
            list_state = ['Sao Paulo', 'Minas Gerais', 'Amazonas', 'Rio de Janeiro', 'Parana']
            result = choice(list_state)
            file = open('database2.txt', 'a', encoding = 'utf-8')
            file.write(f'{result}\n')
            print()
            print(f'Data {result} inserted on the file with success.')
            file.close()
        print()
        input('Press anything to continue.')
        system('cls')
