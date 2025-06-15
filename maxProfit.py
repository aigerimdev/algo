def max_profit(prices):
    # [7,3,5,2,6,4] -> 5. (6-1=5)
    left = 0 # to buy
    right = 1 # to sell
    highest_profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            highest_profit = max(highest_profit, profit)
        else:
            left = right
        right += 1
    return highest_profit

print(max_profit([7,3,5,2,6,4]))