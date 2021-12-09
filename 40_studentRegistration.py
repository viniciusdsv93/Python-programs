# Program that creates a student registration using POO

from time import sleep
from os import name, system

# create the class Student with some attributes and methods

class Student():
    def __init__(self, name):
        self.name = name

    def newStudent(self, name):
        with open('students.txt', 'r') as registry:
            wholeFile = registry.read().split()
            wholeFile.append(name)
            wholeFile.sort()
        with open('students.txt', 'w') as registry:
            pass
        for word in wholeFile:
            with open('students.txt', 'a+') as registry:
                registry.write(f'{word} \n')
        print('Student successfully registered.\n')
        input('Press anything to continue.')
        system('cls')

    def delStudent(self, name):
        with open('students.txt', 'r') as registry:
            wholeFile = registry.read().split()
            if name not in wholeFile:
                print('Sorry. Student not found.\n')
                input('Press anything to continue.')
                system('cls')
            else:
                wholeFile.remove(name)
                with open('students.txt', 'w') as registry:
                    pass
                for word in wholeFile:
                    with open('students.txt', 'a+') as registry:
                        registry.write(f'{word} \n')
                print('Student successfully removed.\n')
                input('Press anything to continue.')
                system('cls')

    def showStudentsList(self):
        with open('students.txt', 'r') as registry:
            print(registry.read())
            input('Press anything to continue.')
            system('cls')

# create a menu and ask the users their option
# insert new student, delete student, show student's list or exit
# use a loop to repeat the program while the exit option is not selected

while True:
    print()
    print('=' * 10,'STUDENT REGISTRY','=' * 10)
    option = input('''\nSelect one of the following options:

[1] - Register new student
[2] - Delete student
[3] - Show the complete students list
[4] - Exit\n''')
    if option == '1':
        studentsName1 = input('\nEnter the student\'s name: \n')
        student1 = Student(studentsName1)
        student1.newStudent(studentsName1)
    elif option == '2':
        studentsName2 = input('\nEnter the student\'s name: \n')
        student2 = Student(studentsName2)
        student2.delStudent(studentsName2)
    elif option == '3':
        student = Student(name)
        student.showStudentsList()
    elif option == '4':
        break
    else:
        print('\nInvalid option')
        input('Press anything to continue.')
        system('cls')

print('\nClosing program...\n')
sleep(1)
