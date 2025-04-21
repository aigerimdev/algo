# option 1
def is_number(arr):
    for char in arr:
        if isinstance(char, (int, float)):
            return True
    return False

print(is_number(['aika', "1"]))


#option 2
def is_number(arr):
    for char in arr:
        if type(char) == int or type(char) == float:
            return True
        return False
    
print(is_number(['aika', "1"]))