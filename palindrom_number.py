def isPalindrome(num):
    num = str(num) 
    for i in range(len(num) // 2):
        if num[i] != num[-i-1]:
            return False
    return True  

print(isPalindrome(12321))