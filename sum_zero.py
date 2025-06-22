"""writea funct which accepts a sorted array of intigers. THe funct should find the first pair the sum is 0.
Return an array that includes both values that sum to zero or undefined if pair does not exist"""
def sum_zero(nums):
    # two pointers to compare
    # while loop from start and end
    # if left num + right num == 0:
    # return noth of thise nums
    
    left = 0
    right = len(nums) -1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == 0:
            return nums[left], nums[right]
        elif sum > 0:
            right -= 1
        else:
            left += 1
            
print(sum_zero([-4, -3, -2, -1, 0, 1, 2, 3, 10]))