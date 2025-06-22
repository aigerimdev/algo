def plusOne(digits):
    # Input: digits = [1,2,3]
    # Output: [1,2,4]
    # loop trough each digit and add them to str
    # convert str to num
    # add 1
    # convert that digit to str
    # string -> list
    # restunr that
    num_str = ""
    for num in digits:
        num_str += str(num)
    num = int(num_str) + 1
    
    result = []
    for n in str(num):
        result.append(int(n))
    return result
    
digits=[1, 2, 3]
print(plusOne(digits))