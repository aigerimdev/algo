"""Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]"""

def search_ranges(nums, target):
    # define a pointers left, right 
    # loop through the list of numbers 
    # compare the items with target 
        # if target excist then pointers are gonna be updated
    left = -1
    right = -1
    for i, num in enumerate(nums):
        if num == target:
            if left == -1:
                left = i
            right = i
    return [left, right]
print(search_ranges([5,7,7,8,8,10], 8))



