
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
print(searchInsert([1, 2, 3, 4, 5], 3)) # expected 2