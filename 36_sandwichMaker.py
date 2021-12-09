# Program that asks the users for their sandwich preferences and calculate the price.

import pyinputplus as pyip

# use a menu to ask their bread, protein type and other preferences.

print('==' * 20)
print('SANDWICH MAKER'.center(40))
print('==' * 20, '\n')

totalCost = 0

breadOption = pyip.inputMenu(['wheat - US$ 2.00', 'white - US$ 2.00', 'sourdough - US$ 2.50'], numbered = True)

if breadOption == 'wheat - US$ 2.00':
    totalCost += 2.00
elif breadOption == 'white - US$ 2.00':
    totalCost += 2.00
elif breadOption == 'sourdough - US$ 2.50':
    totalCost += 2.50

proteinOption = pyip.inputMenu(['chicken - US$ 4.50', 'turkey - US$ 7.25', 'ham - US$ 6.75', 'tofu - US$ 3.60'], numbered = True)

if proteinOption == 'chicken - US$ 4.50':
    totalCost += 4.50
elif proteinOption == 'turkey - US$ 7.25':
    totalCost += 7.25
elif proteinOption == 'ham - US$ 6.75':
    totalCost += 6.75
elif proteinOption == 'tofu - US$ 3.60':
    totalCost += 3.60

cheeseOption = pyip.inputYesNo('Do you want cheese? ')

if cheeseOption == 'yes':
    cheeseType = pyip.inputMenu(['cheddar - US$ 2.20', 'swiss - US$ 4.30', 'mozzarella - US$ 1.70'], numbered = True)
    if cheeseType == 'cheddar - US$ 2.20':
        totalCost += 2.20
    elif cheeseType == 'swiss - US$ 4.30':
        totalCost += 4.30
    elif cheeseType == 'mozzarella - US$ 1.70':
        totalCost += 1.70

additionOption = pyip.inputMenu(['mayo - US$ 0.70', 'mustard - US$ 0.65', 'lettuce - US$ 1.20', 'tomato - US$ 2.40', 'None'], numbered = True)

if additionOption == 'mayo - US$ 0.70':
    totalCost += 0.70
elif additionOption == 'mustard - US$ 0.65':
    totalCost += 0.65
elif additionOption == 'lettuce - US$ 1.20':
    totalCost += 1.20
elif additionOption == 'tomato - US$ 2.40':
    totalCost += 2.40
elif additionOption == 'None':
    pass

# ask how many sandwiches they want.

totalSandwichesOption = pyip.inputInt('How many sandwiches do you want?', min = 1)
totalCost = totalCost * totalSandwichesOption

# print the total cost.

print(f'\nTotal cost: US$ {totalCost:.2f}.\n')
