def get_missing_numbers_in_range(array, low, high):
    hash_table = {num: True for num in array}
    missing = []
    
    for i in range(low, high):
        if i not in hash_table:
            missing.append(i)
    return missing