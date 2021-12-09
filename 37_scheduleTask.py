import time

def calcProd():
    # calculate the product of the first 100 numbers
    product = 1
    for i in range(1, 100):
        product = product * i
    return product

startTime = time.time()

prod = calcProd()

endTime = time.time()

print(f'The result is {prod} and it\'s {len(str(prod))} digits long')
print(f'Took {endTime - startTime} seconds to calculate it.')
print(time.ctime())
