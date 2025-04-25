def is_permutation(word1, word2):
    # If lengths don't match, can't be a permutation
    if len(word1) != len(word2):
        return False

    # Count letters in word1
    hash_table = {}
    for char in word1:
        hash_table[char] = hash_table.get(char, 0) + 1

    # Subtract letter counts using word2
    for char in word2:
        if char not in hash_table:
            return False
        hash_table[char] -= 1
        if hash_table[char] < 0:
            return False

    return True