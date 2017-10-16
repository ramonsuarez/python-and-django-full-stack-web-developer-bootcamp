print('Welcome to Code Breaker\nGuess the right 3 digit number with the help of the hints')
# Generate number
import random
digits = list(range(10))
random.shuffle(digits)
target = (digits[:3])
print ('Target test: {}'.format(target))

# Ask for user's numbers until right solution
gotIt = False
answer = input("What's your guess? ")
while gotIt != True:
    answer_array = [int(i) for i in str(answer)]
    if answer_array == target:
        print('Ole! You guessed the number right, it was {}'.format(answer))
        gotIt = True
    elif (lambda x: x in set(target), answer_array ):
        print('Here is the result of your guess:\n Match')
        answer = input("What's your new guess? ")
        gotIt = False
