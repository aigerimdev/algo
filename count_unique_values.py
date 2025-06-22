"""func which acceots a sorted array and counts the unique values in the array.
There can be nagative numbers in the array, but it will always be soreted"""
def count_uniqe(nums):
    #[1, 1, 1, 2, 3, 4, 5, 6, 6, 6]
    #          i  j
    # counter
    # two pointer
    if not nums:
        return None
    left = 0
    right = 1
    counter = 0
    
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
        else:
            counter += 1
            left = right
            right += 1
    return counter + 1

print(count_uniqe([1, 1, 1, 2, 3, 4, 5, 6, 6, 6]))