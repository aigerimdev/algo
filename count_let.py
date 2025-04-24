# input word = "banana", letter = "a"

#output -> 3

# option1
def count_letter(word, letter):
    counter = 0
    for i in range(len(word)):
        if word[i] == letter:
            counter += 1
    return counter
print(count_letter("banana", "a"))


# option2
def count_letter(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter
print(count_letter("banana", "a"))