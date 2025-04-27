def pairs_with_given_sum (numbers, target):
    if not numbers:
        return 0
    
    if not all(isinstance(num, int) for num in numbers) or not isinstance(target, int):
        raise ValueError("You can enter only numbers and the target must be an integer!")
    
    if len(numbers) == 1:
        return 0
    
    hash_table = {}
    counter = 0
    
    for num in numbers:
        complement = target - num
        
        if complement in hash_table:
            counter += 1    
        hash_table[num]= True
        
    return counter
