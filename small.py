def find_smallest(numbers):
    smallest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(find_smallest([8, 4, 6, 9, 5, 7]))