def romanToInt(s):
    roman={"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
    number=0
    for i in range(len(s)-1):
        print(roman[s[i]])
        if roman[s[i]] < roman[s[(i+1)]]:
            number-=roman[s[i]]
        else:
            number+=roman[s[i]]
    return number+roman[s[-1]]
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
s = "LVIII"

print(romanToInt(s))