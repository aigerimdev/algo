def factorial(n):
    if n == 0:
        return 1
    if n < 1:
        raise ValueError
    return n * factorial(n-1)

# factorial(4-1)
#     factorial(3-1)
#         factorial(2-1)
#             1
#         2 *
#     3 *
# 4 *
# # 4 * 3 * 2 * 1 = 24
bunny(3-1)
    bunny(2-1)
        bunny(1-1)
        1 +2
    2+2
3+2