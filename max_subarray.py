"""funct sccepts an array of integers and a number called n.
The func should calculate the max sum of n consecuitive elements in the array."""

def max_subarray(arr, n):
    if len(arr) < n:
        return None

    max_sum = sum(arr[:n])
    temp_sum = max_sum

    for i in range(n, len(arr)):
        temp_sum = temp_sum - arr[i - n] + arr[i]
        max_sum = max(max_sum, temp_sum)

    return max_sum

print(max_subarray([1, 2, 5, 2, 8, 1, 5], 2))  # Output: 10
