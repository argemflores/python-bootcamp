# array123

# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
    next_num = 1
    last_num = 3
    
    for num in nums:
        if num == next_num and num <= 3:
            next_num += 1
    
    return next_num == 4
