# Option1
def count_vowels(word):
    counter = 0
    list_of_vowels = {"a", "e", "i", "o", "u"} # set is faster than tuple
    
    for char in word:
        if char in list_of_vowels:
            counter += 1
    return counter

print(count_vowels("aigerim"))

# Option2
def count_vowels(word):
    counter = 0
    
    for char in word:
        if char in ("a", "e", "i", "o", "u"): # tuple is slower than set
            counter += 1
    return counter

print(count_vowels("aigerim"))
    