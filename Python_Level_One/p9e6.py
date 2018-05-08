def count_evens(nums):
    evens = filter(lambda nums: nums % 2 == 0, nums)
    return len(evens)
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
