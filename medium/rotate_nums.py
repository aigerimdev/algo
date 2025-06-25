"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
def rotate(nums, k):
    # slice k size of nums from right to  left
    # push that piece to the beginning of my array
    last_part = nums[-k:] # [5, 6, 7]
    first_part = nums[:-k] # [1, 2, 3, 4]   
    result = last_part + first_part # [5, 6, 7, 1, 2, 3, 4]
    return result
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))