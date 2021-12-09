from os import system
from time import sleep

def headline(msg, size = 50):
    print('=' * size)
    print(f'{msg}'.center(size))
    print('=' * size + '\n')

def register():
    system('cls')
    headline('LOGIN SYSTEM')
    try:
        file = open('username_database.txt', 'r')
    except FileNotFoundError:
        file = open('username_database.txt', 'w+')
    
    username = input('Create username: ')
    password = input('Create a password: ')
    confirm_password = input('Confirm password: ')
    list_username = []
    list_password = []
    for i in file:
        un, pw = i.split(', ')
        pw = pw.strip()
        list_username.append(un)
        list_password.append(pw)

    if password != confirm_password:
        print()
        print("Passwords don't match.")
        print()
        input('Press anything to continue.')
        system('cls')
        register()
        headline('LOGIN SYSTEM')
    else:
        if len(password) < 6:
            print()
            print('Password too short. Please, try again.')
            print()
            input('Press anything to continue.')
            system('cls')
            register()
        
        elif username in list_username:
            print()
            print('Username in use. Please, try again.')
            print()
            input('Press anything to continue.')
            system('cls')
            register()
        else:
            with open('username_database.txt', 'a') as file:
                file.write(f'{str(username)}, {str(password)}\n')
                print('Username created with success.')
                print()
                input('Press anything to continue.')
                system('cls')

def access():
    system('cls')
    headline('LOGIN SYSTEM')
    username = input('Please, enter your username: ')
    password = input('Please, enter your password: ')
    list_username = []
    list_password = []
    with open('username_database.txt', 'r') as file:
        for i in file:
            un, pw = i.split(', ')
            pw = pw.strip()
            list_username.append(un)
            list_password.append(pw)
    print(list_username)
    print(list_password)

    if username not in list_username:
        print()
        print('Username not registered. Please, try again.')
        print()
        input('Press anything to continue.')
        system('cls')
        headline('LOGIN SYSTEM')
        access()
    else:
        if password not in list_password:
            print()
            print('Error. Wrong username or password. Please, try again.')
            print()
            input('Press anything to continue.')
            system('cls')
            access()
            headline('LOGIN SYSTEM')
        elif list_username.index(username) != list_password.index(password):
            print()
            print('Error. Wrong username or password. Please, try again.')
            print()
            input('Press anything to continue.')
            system('cls')
            headline('LOGIN SYSTEM')
            access()
        elif list_username.index(str(username)) == list_password.index(password):
            print()
            print('Access granted.')
            print()
            input('Press anything to continue.')
            system('cls')

def home():
    system('cls')
    headline('LOGIN SYSTEM')
    option = input('Do you want to login or register? [L/R] ').strip().upper()[0]
    print()
    if option == 'L':
        access()
    elif option == 'R':
        register()
    else:
        print('Please, enter a valid option.')
        print()
        input('Press anything to continue.')
        system('cls')
        home()

while True:
    system('cls')
    home()
    headline('LOGIN SYSTEM')
    option = input('Continue? [Y/N] ').strip().upper()[0]
    print()
    if option in "N":
        system('cls')
        print('Closing program... \n')
        sleep(1)
        break