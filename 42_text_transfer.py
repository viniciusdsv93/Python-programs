# Program that transfers text from a file to another.

with open('text1.txt', 'r') as file1:
    sample = file1.read()

with open('text2.txt', 'a') as file2:
    file2.write(sample)
    print(file2.read())

with open('text2.txt', 'r') as file2:
    print(file2.read())
    