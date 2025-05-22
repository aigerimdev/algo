def unique_occurrence(arr):
    # create a hash table to see frequency of items {"1": 3}
    hash_table = {}
    for num in arr:
        if num in hash_table:
            hash_table[num]+= 1
        else:
            hash_table[num] = 1
        
    # gets how many times each number appeared [3, 2, 2]
    all_counts = hash_table.values() 
    unique_counts = set(all_counts) # {2, 3}

    if len(unique_counts) == len(all_counts):
        return True
    else:
        return False

print(unique_occurrence([1,2,2,1,1,3,3]))