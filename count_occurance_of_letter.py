def count_occur(inp, target):
    counter = 0 
    
    for char in inp:
        if char == target:
            counter += 1
    return counter
    
print(count_occur([1, 2, 3, 2, 5, 2], 2))
print(count_occur("aigerim", "i"))