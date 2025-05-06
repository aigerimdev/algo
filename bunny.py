def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)