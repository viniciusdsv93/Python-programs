from file_manipulator import *
from utilities import *
from os import system
from time import sleep

look_for_file('database.txt') # Check if there is a specific file. If not, creates one

while True:
    headline('DATA GENERATOR', 50)
    format_menu([
        'Show data',
        'Generate new data',
        'Exit'
    ], 50)
    
    option = main_menu_option()
    system('cls')

    if option == 1:
        headline('DATA LIST', 50)
        read_file('database.txt')
        input('Press anything to go back.')
        system('cls')

    elif option == 2:
        headline('GENERATE NEW DATA')
        secondary_menu('Name', 'Email', 'Cel phone', 'City', 'State')
        secondary_option = register_option()
        draw = draw_data(secondary_option)
        write_in_file('database.txt', draw)
        input('Press anything to go back.')
        system('cls')
    
    elif option == 3:
        system('cls')
        print('Closing program...')
        sleep(2)
    
    if option == 3:
        break