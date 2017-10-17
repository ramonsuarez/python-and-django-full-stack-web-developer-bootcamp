print('Welcome to Code Breaker\nGuess the right 3 digit number with the help of the hints')
# Generate number
import random
digits = list(range(10))
random.shuffle(digits)
nums = [str(i) for i in str(digits[:3]) if i.isdigit()]
target = []
for num in nums:
    target += num
# TEST
print ('Target: {}'.format(target))
print(type(target))
# DRY question function to get guess from user
# Had to use raw_input because of Python 3 not accepting leading 0
def question():
    return list(str(raw_input("What's your guess? ")))
# In case the number is longer than 3 digits, only take the first 3 digits
answer = question()[:3]

# Match function
def match():
    for i, a in enumerate(answer):
        if a == target[i]:
            return (True,)
# # Close function
def close():
    for i in answer:
        if i in target:
            return (True,)
# Ask for user's numbers, loop until right solution
gotIt = False
while gotIt == False:
    # Correct answer
    if answer == target:
        print('Ole! You guessed the number right, it was {}'.format(answer))
        gotIt = True
    #     Match: You've guessed a correct number in the correct position

    elif match() :
        # elif (lambda x: target(x) == answer(x),answer):
        for True in match():
            print('Tip: Match')
        answer = question()[:3]
        # elif (lambda x: answer(x) not in target, answer):
        #     Close: You've guessed a correct number but in the wrong position
    elif close():
        for True in close():
            print('Tip: Close')
        answer = question()[:3]
    # Nope: You haven't guess any of the numbers correctly
    else:
        print('Tip: Nope')
        answer = question()[:3]
