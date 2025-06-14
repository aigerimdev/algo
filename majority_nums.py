def majorityElement(nums):
        # loop trought the nums
        freq_num = {} # {3: 2, 2:1}
        for num in nums:
            if num not in freq_num:
                freq_num[num] = 1
            else:
                freq_num[num] += 1
                
        return max(freq_num, key=freq_num.get)
    
    # max_count = 0
    # majority = None
    # for num in freq:
    #     if freq[num] > max_count:
    #         max_count = freq[num]
    #         majority = num

    # return majority

print(majorityElement([3,3,4]))