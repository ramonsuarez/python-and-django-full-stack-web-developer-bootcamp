def arrayCheck(nums):
    ott = [1,2,3]
    for ind, val in enumerate(nums):
        if ind <= (len(nums)-3):
            numSlice = [nums[ind], nums[ind+1],nums[ind+2]]
            if numSlice == ott:
                return True
    return False
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))
