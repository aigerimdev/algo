def apple(apples):
    if apple == 1:
        return 1
    print("Calling apple! apples:", apples)
    return apple(apples - 1)

def list_length(my_list):
    if my_list == []:
        return 0
    return 1 + list_length(my_list[1:])

data = [1, 2, 3, 4, 5]
print(list_length(data))

def list_length(my_list, pos=0):
    try:
        my_list[pos]
    except IndexError:
        return pos 
    return list_length(my_list, pos + 1)
    

data = [1, 2, 3, 4, 5]
print(list_length(data))

# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    if len(parens) % 2 != 0:
        return False
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    return False


# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <=1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    last1 = num1 % 10
    last2 = num2 % 10

    match = 1 if last1 == last2 else 0

    # base case: stop when one number runs out
    if num1 < 10 or num2 < 10:
        return match

    return match + digit_match(num1 // 10, num2 // 10)