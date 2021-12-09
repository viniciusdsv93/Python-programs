# Program that prints a table from a list of lists, with right-justified columns.

def printTable(list):

    # find the lenght of the longest word.

    max = 0
    maxList = []
    for x in range(0, 3):
        for y in range(0, 4):
            if len(list[x][y]) > max:
                max = len(list[x][y])
        maxList.append(max)
        max = 0
    
    # print a table with the items right-justified according to that lenght.

    for x in range(0, 4):
        print()
        for y in range(0, 3):
            print(list[y][x].rjust(maxList[y]), end = ' ')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

print('\n')
