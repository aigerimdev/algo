# option 1 bettter short, easy to read fast
def reverse_word(word):
    return word[::-1]
print(reverse_word("aigerim"))

#option 2
def reverse_word(word):
    reversed_char = reversed(word)
    return "".join(reversed_char)
print(reverse_word("aigerim"))