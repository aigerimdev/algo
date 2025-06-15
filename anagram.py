def isAnagram(s, t):
    # s = "anagram", t = "nagaram" -> true
    s = list(s)
    t = list(t)
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    print(sorted_s)

    if sorted_s == sorted_t:
        return True
