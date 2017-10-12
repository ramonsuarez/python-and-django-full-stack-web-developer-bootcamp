       
    ott = (1,2,3)
    if ott in nums:
        return True
    else:
        return False
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))
=======
def doubleChar(str):
    newStr = ''
    for char in str:
        newStr = newStr + char * 2
    return newStr

doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')
