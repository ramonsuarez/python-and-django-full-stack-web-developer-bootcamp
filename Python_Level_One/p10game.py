print('Welcome to Code Breaker\nGuess the right 3 digit number with the help of the hints')
# Generate number
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])
# Ask for user's numbers until right solution
gotIt = False
while gotIt != True:
    answer = input("What's your guess?")
    # Check answer and provide tips
    if answer == digits[:3]:
        print('Ole!')
        break
    if answer == 111:
        break
