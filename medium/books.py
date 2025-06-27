
# How many books can I buy at most?


def max_books(prices, budget):
    sorted_prices = sorted(prices)
    count = 0
    total = 0
    
    for price in sorted_prices:
        total+= price
        if total <= budget:
            count += 1
        else:
            break
    return count
prices = [10, 20, 5, 8, 15]
budget = 30
print(max_books(prices, budget))
# Output: 3
# Explanation: Buy books with prices 5, 8, 15 → total = 28