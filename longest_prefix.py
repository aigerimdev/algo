"""
LONGEST COMMON PREFIX

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""
def longest_common_prefix(strs):
    pass


assert longest_common_prefix(['flower', 'flow', 'flight']) == "fl"
assert longest_common_prefix(["dog", "cat", "fish"]) == ""
assert longest_common_prefix(["test", "test", "test"]) == "test"
assert longest_common_prefix(["interview", "intermediate", "internet"]) == "inter"
assert longest_common_prefix(["", "prefix", "prelude"]) == ""
print("All tests passed!")

























# hints:
    # You can use first string as baseline
    # Character-by-Character Comparison








# my solution:

# def longest_common_prefix(strs):
#     # Use the first word as reference
#     first_word = strs[0]
#     common_prefix = ''
    
#     # Loop through each character index in the first word
#     for i in range(len(first_word)):
#         char = first_word[i]
#         # Compare with the same position in all other words
#         for word in strs[1:]:
#             # If index is out of range or characters don’t match, stop
#             if i >= len(word) or word[i] != char:
#                 return common_prefix
#         # If all matched, add the character to the result       
#         common_prefix += char
#     return common_prefix