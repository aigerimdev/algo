def is_palindrome(x):
    x = str(x)   
    left = 0
    right = len(x)-1

    while left < right:
        if x[left] == x[right]:
            return True
        left += 1
        right -= 1
    return False
    
x = 121
x = 1217
print(is_palindrome(x))