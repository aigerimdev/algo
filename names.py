def get_missing_numbers_in_range(array, low, high):
    hash_table = {num: True for num in array}

    missing = []  

    for num in range(low, high):
        if num not in hash_table:
            missing.append(num)

    return missing