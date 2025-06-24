
# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_common_prefix(words):
    # loop trough the list of str
    # group the characters by indexes
    # use set to check if the chars are the same
    # if it is the add that char to result var
    # otherwise stop
    # return that result var
    common_prefix = ''
    for chars in zip(*words):
        single_chars = set(chars)
        if len(single_chars) == 1:
            common_prefix += chars[0]
        else:
            break
    return common_prefix
words = ["flower","flow","flight"]
print(longest_common_prefix(words))
    
