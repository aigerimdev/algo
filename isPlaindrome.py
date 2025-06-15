
def isPalindrome(s):
    # convert to lower case
    # remove all characters beside alpha, numbers as well
    # use two pointers and compare from beginning and from end
    # if the caracters are == return true otherwise false

    s = s.lower()

    s = ''.join([char for char in s if s.isalnum()])


    left = 0
    right = len(s)

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(isPalindrome("A man, a plan, a canal: Panama"))