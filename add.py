def add_all_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all_numbers([1, 2, 3, 4]))

# option 2
def add_all_numbers(numbers):
    total = 0
    for i in range(0, len(numbers)):
        total+= numbers[i]
    return total

print(add_all_numbers([1, 2, 3, 4]))

# Option 3
def add_all_numbers(numbers):
    return sum(numbers)

print(add_all_numbers([1, 2, 3, 4]))