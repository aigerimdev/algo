def merge_two_sorted_list(list1, list2):
    result = []
    for num1 in list1:
        for num2 in list2:
            result.append(num1, num2)
    return result
print(merge_two_sorted_list([1,2,4], [1,3,4]))