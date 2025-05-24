def longestCommonPrefix(strs):
    # Use the first word as reference
    first_word = strs[0]
    common_prefix = ''
    
    # Loop through each character index in the first word
    for i in range(len(first_word)):
        char = first_word[i]
        # Compare with the same position in all other words
        for word in strs[1:]:
            # If index is out of range or characters don’t match, stop
            if i >= len(word) or word[i] != char:
                return common_prefix
        # If all matched, add the character to the result       
        common_prefix += char
    return common_prefix
    
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["prefix", "", "prelude"]))
print(longestCommonPrefix(["test", "test", "test"]))
