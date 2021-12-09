# Program that generates a multiplication quiz.

import random, time, pyinputplus as pyip

# create a for loop to ask 10 multiplication questions to the user.

totalnNumQuestions = 10
correctAnswers = 0

for actualQuestion in range(totalnNumQuestions):
    num1 = random.randint(1, 9) 
    num2 = random.randint(1, 9)
    try:
        answer = pyip.inputNum(f'\n{actualQuestion + 1}: {num1} x {num2} = ', timeout = 8)
    except pyip.TimeoutException:
        print('Out of time.')
    if answer == num1 * num2:
        print('Correct!')
        time.sleep(1)
        correctAnswers += 1     # keep track of the number of correct answers.
    else:
        print('Wrong!')
        time.sleep(1)

# print the user's results.

print(f'\nFinal score: you answered correctly {correctAnswers} out of {totalnNumQuestions} questions.\n')
