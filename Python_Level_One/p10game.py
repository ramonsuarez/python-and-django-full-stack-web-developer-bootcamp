print('Welcome to Code Breaker\nGuess the right 3 digit number with the help of the hints')
# Generate number
import random
digits = list(range(10))
random.shuffle(digits)
target = [str((digits[:3]))]
print ('Target test: {}'.format(target))
# DRY question function to get guess from user
def question():
    return list(str(input("What's your guess? ")))
answer = question()
# Test
print(answer)
# Ask for user's numbers until right solution
gotIt = False
while gotIt = False:
    #     Close: You've guessed a correct number but in the wrong position
    #     Match: You've guessed a correct number in the correct position
    #     Nope: You haven't guess any of the numbers correctly



    # if answer == str(target):
    #     print('Ole! You guessed the number right, it was {}'.format(answer))
    #     gotIt = True
    # elif (lambda x: answer(x) not in str(target), answer):
    #     print('Here is the result of your guess:\n Nope')
    #     answer = question()
    # elif (lambda x: str(target)(x) == answer(x),answer):
    #     print('Here is the result of your guess:\n Match')
    #     answer = question()
    # else:
    #     print('Here is the result of your guess:\n Close')
    #     answer = question()
