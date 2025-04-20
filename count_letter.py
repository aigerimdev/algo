#option 1
def count_letter(word):
    total_letter = len(word)
    return total_letter
print(count_letter("aigerim"))

# option 2
def count_letter(word):
    total_letter = 0
    
    for char in word:
        total_letter += 1
    return total_letter
print(count_letter("aigerim"))