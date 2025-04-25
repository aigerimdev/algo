def get_intersection(list1, list2):
    table = {num: True for num in list1}
    intersection = []

    for num in list2:
        if num in table:
            intersection.append(num)

    return intersection