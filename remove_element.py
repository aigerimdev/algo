def removeElement(nums, val):
    if not nums:
        return 0 
    counter = 0
    for num in nums:
        if num != val:
            nums[counter] = num
            counter += 1
    return counter

print(removeElement([0,1,2,2,3,0,4,2], 2))