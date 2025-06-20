def is_anagram(str1, str2):
    # declare a variable {}
    # for loop str1 and see freq of it
    # loop through second str2 and 
    # if char in freq map -1
    # if the hash is empty at the end return true 
    # otherwise false
    hash = {}
    for char in str1:
        if char not in hash:
            hash[char] = 1
        else:
            hash[char] += 1
    print(hash)
    for letter in str2:
        if letter not in hash:
            return False
        else:
            hash[letter] -= 1
            
    print(hash)
    for key, value in hash.items():
        if value != 0:
            return False
    return True

print(is_anagram('azz', 'zza'))