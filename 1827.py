"""
1827. Minimum Operations to Make the Array Increasing

You are given an integer array nums (0-indexed). In one operation, you can choose an element of the
array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of
length 1 is trivially strictly increasing.

"""


# Bruteforce
def count_incres(arr):
    i, count = 0, 0
    while i >= 0 and i < len(arr) - 1:
        j = i + 1
        if arr[i] < arr[j]:
            i += 1
        else:
            x = arr[i] + 1
            count += x - arr[j]
            arr[j] = x
            i += 1
    print(count)


count_incres(arr)


# Optimised 
def min_count(nums):
    prev = 0
    ans = 0
    for num in nums:
        if num > prev:
            prev = num
        else:
            prev = prev + 1
            ans += prev - num
    print(ans)


min_count(arr)
