# Program that creates a virtual pet using OOP

from random import randint
from time import sleep
from os import system

# create class and methods
class VirtualPet():
    def __init__(self, name, hunger = randint(0, 100), boringness = randint(0, 100)):
        self.name = str(name)
        self.hunger = hunger
        self.boringness = boringness
        print('\nVirtual Pet successfully created!')

    def feedPet(self):
        print(f'\nFeeding {self.name}...')
        sleep(2)
        self.hunger -= 20
        self.boringness += 10

    def playPet(self):
        print(f'\nPlaying with {self.name}...')
        sleep(2)
        self.boringness -= 20
        self.hunger += 15

    def showStatus(self):
        if self.hunger >= 100:
            print('\nYour VirtualPet starved to death! You are a horrible person!')
        elif self.boringness >= 100:
            print('\nYour VirtualPet got bored and fell asleep...')
        else:
            print(f'''\n{self.name}\'s status:
Hunger: {self.hunger}
Boringness: {self.boringness}\n''')

    def doNothing(self):
        print('Your pet is getting hungry and bored...')
        self.hunger += 20
        self.boringness += 20
        sleep(2)

# create an object of that class
# inform the user how to interact with the virtual pet

while True:    
    print('=' * 15, 'VIRTUAL PET', '=' * 15)
    print('''\nBe careful. If your pet\'s hunger reaches 100
he or she is going to die! Also, if the
boringness status reaches 100 he or she
is going to fell asleep.\n''')

    option = input('''\nPlease, enter one of the following options:
[1] - Create a new Virtual Pet
[2] - Show pet's status
[3] - Feed pet
[4] - Play with pet
[5] - Do nothing
[6] - Exit
''')
    if option == '1':
        pet1Name = str(input('\nEnter your pet\'s name: '))
        pet1 = VirtualPet(pet1Name)
        input('Press anything to continue.')
        system('cls')
    elif option == '2':
        pet1.showStatus()
        input('Press anything to continue.')
        system('cls')
    elif option == '3':
        pet1.feedPet()
        input('Press anything to continue.')
        system('cls')
    elif option == '4':
        pet1.playPet()
        input('Press anything to continue.')
        system('cls')
    elif option == '5':
        pet1.doNothing()
        input('Press anything to continue.')
        system('cls')
    elif option == '6':
        print('\nSee you next time! Bye!\n')
        sleep(1)
        break
    else:
        print('\nInvalid option.\n')
        