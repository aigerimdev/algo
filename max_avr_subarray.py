"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000"""

def find_max_subarray(nums, k):
    # Start with first k elements
    sum_of_nums = sum(nums[:k])
    max_sum = sum_of_nums

    # Slide the window
    for i in range(k, len(nums)):
        sum_of_nums = sum_of_nums - nums[i - k] + nums[i]
        max_sum = max(max_sum, sum_of_nums)

    return max_sum / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(find_max_subarray(nums, k))
