def get_intersection(list1, list2):
    table = {num: True for num in list1}
    intersection = []

    for num in list2:
        if num in table:
            intersection.append(num)

    return intersection

def get_intersection(list1, list2):
    intersection = []

    for num in list2:
        if num in list1:
            intersection.append(num)

    return intersection
#An example of a working implementation:

def get_intersection(red, blue):
    frequency_hash = {}

    for list in [red, blue]:
        for item in list:
            if item in frequency_hash:
                frequency_hash[item] += 1
            else:
                frequency_hash[item] = 1

    intersections = []
    for item, quantity in frequency_hash.items():
        if quantity > 1:
            intersections.append(item)

    return intersections

#Another example of a working implementation:

def get_intersection(red, blue):
    frequency_hash = {}

    for list in [red, blue]:
        for item in list:
            count = frequency_hash.get(item, 0)
            frequency_hash[item] = count + 1

    intersections = []
    for item, quantity in frequency_hash.items():
        if quantity > 1:
            intersections.append(item)

    return intersections