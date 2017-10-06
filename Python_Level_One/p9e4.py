def arrayCheck(nums):
       
    ott = (1,2,3)
    if ott in nums:
        return True
    else:
        return False
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))
