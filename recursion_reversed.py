def reverse(text):
    if text == "":
        return ""
    return text[-1] + reverse(text[:-1])
    

# option 2
def reverse(text):
    if len(text) <= 1:
        return text
    # Use Python string slicing to get the
    # first character of text and the
    # remaining characters
    first_char = text[:1]
    remaining_chars = text[1:]
    return reverse(remaining_chars) + first_char