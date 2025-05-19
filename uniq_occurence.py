def unique_occurence(arr):
    hash_table = {}
    # count how many times each number appears
    for num in arr:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    # check for unique counts
    seen = set()
    for count in hash_table.values():
        if count in seen:
            return False
        seen.add(count)

    return True

print(unique_occurence([1,2,2,1,1,3,3]))