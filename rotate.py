def rotate_list(list, shift_by):
    if not list or shift_by == 0:
        return list
    
    right_part = list[-shift_by:]
    left_part = list[:-shift_by]
    return right_part + left_part

print(rotate_list([1, 2, 3], 2))
print(rotate_list(['a', 'b', 'c', 'd'], 1))
print(rotate_list(['u', 16, 'hello', 27], 3))
print(rotate_list([], 3))