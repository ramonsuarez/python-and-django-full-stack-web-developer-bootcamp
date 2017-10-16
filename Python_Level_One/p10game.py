print('Welcome to Code Breaker\nGuess the right 3 digit number with the help of the hints')
# Generate number
import random
digits = list(range(10))
random.shuffle(digits)
nums = [str(i) for i in str(digits[:3]) if i.isdigit()]
print(nums)
target = []
for num in nums:
    target += num
    print(target)
# target = (lambda i: str(i) in nums, nums)
print ('Target test: {}'.format(target))
# DRY question function to get guess from user
# Had to use raw_input because of Python 3 not accepting leading 0
def question():
    print list(str(raw_input("What's your guess? ")))
answer = question()
# Ask for user's numbers until right solution
gotIt = False
while gotIt == False:
    #     Close: You've guessed a correct number but in the wrong position
    #     Match: You've guessed a correct number in the correct position
    #     Nope: You haven't guess any of the numbers correctly
    if answer == target:
        print('Ole! You guessed the number right, it was {}'.format(answer))
        gotIt = True
    elif (lambda x: target(x) == answer(x),answer):
        print('Here is the result of your guess:\n Match')
        answer = question()
    elif (lambda x: answer(x) not in target, answer):
        print('Here is the result of your guess:\n Nope')
        answer = question()
    else:
        print('Here is the result of your guess:\n Close')
        answer = question()
