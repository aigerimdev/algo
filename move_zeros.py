def moveZeroes(nums):  
# i tracks the position for the next non-zero number
# When we find a non-zero nums[j], we swap it with nums[i]
# Then move i forward
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)