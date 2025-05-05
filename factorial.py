def factorial(n):
    if n == 0:
        return 1
    if n < 1:
        raise ValueError
    return n * factorial(n-1)