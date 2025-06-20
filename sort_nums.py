def sorting(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]> nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums   
nums = [3, 1, 4, 6, 7, 2, 5]
print(sorting(nums))