# Program that create a class and some methods to raise the employees salaries

# create a class
class Employee():
    def __init__(self, name, salary):
        self.name = str(name)
        self.salary = int(salary)
        print('\nObject successfully created.')

    def raiseSalary(self, percent):
        self.salaryRaised = self.salary
        self.salaryRaised += (self.salary * int(percent)) / 100
        

# create an object of that class

employee1name = input('\nEnter the employee\'s name: ')
employee1salary = input('\nEnter the employee\'s salary: ')

# object created using the arguments provided by the user
employee1 = Employee(employee1name, employee1salary)

# call the raiseSalary method in the object using the percentual informed by the user
employee1raise = input('\nEnter the raise to be applied: ')

employee1.raiseSalary(employee1raise)

# print the object's situation
print(f'\nEmployee registered: {employee1.name}, salary with {employee1raise} percent of raise: $ {float(employee1.salaryRaised):.2f}')
print(f'\n{employee1.name}\'s initial salary: $ {float(employee1.salary):.2f}\n')
