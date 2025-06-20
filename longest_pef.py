def longest_string(str):
    # create a hash map
    # loop trough each letter and check in hash
    # create variable to store max length
    # if hash already exist in the hash clear current hash
    # return max length
    hash = {}
    candidate = 0
    max_length = 0

    for char in str:
        if char not in hash:
            hash[char] = True
            candidate += 1
        else:
            max_length = max(max_length, candidate)
            hash = {char: True}
            candidate = 1

    return max(max_length, candidate)
# print(longest_string("abcabcbb"))  # 3 -> "abc"
print(longest_string("bbbbb"))     # 1 -> "b"
# print(longest_string("pwwkew"))    # 3 -> "wke"

