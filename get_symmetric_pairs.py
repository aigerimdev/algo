# [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
def get_symmetric_pairs(pairs):
    map = {}
    
    symmetric_pairs = []
    for num1, num2 in pairs:
        if num2 in map and map[num2] == num1:
            symmetric_pairs.append([num2, num1])
        else:
            map[num1] = num2
    return symmetric_pairs