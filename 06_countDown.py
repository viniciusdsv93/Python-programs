# Program that sets a countdown for the user.

from time import sleep

# ask the user how many seconds they want to countdown.

while True:
    
    seconds = input('\nHow many seconds do you want to countdown? ')

    # ask them to press anything to begin the countdown.

    input('\nPlease, press anything to begin the countdown.\n')

    for s in range(int(seconds), 0, -1):
        print(s)
        sleep(1)

    print('\nTime is over.\n')

    while True:
        option = input('Continue? [Y/N] ').strip().upper()[0]
        if option in 'YN':
            break
    if option == 'N':
        break

print('\nProgram ended.\n')