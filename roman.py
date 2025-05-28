def romanToInt(s):
    available_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    index = 0
    while index < len(s) - 1:
        if available_nums[s[index]] < available_nums[s[index + 1]]:
            total -= available_nums[s[index]]
        else:
            total += available_nums[s[index]]
        index += 1

    total += available_nums[s[-1]]
    return total