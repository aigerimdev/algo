# Example 1:
# "([])" true

# Example 2:
# "([})" false 


# Example 3:
# "6()[]" false


def isValid(s):
    st = []

    for i in range(len(s)):
        if st:
            last = st[-1]
            if is_pair(last, s[i]):
                st.pop()
                continue
        st.append(s[i])
    
    return not st

def is_pair(last, cur):
    if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
        return True
    return False





