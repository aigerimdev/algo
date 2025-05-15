def findKthPositive(arr, k):
        current_num = 1
        missing_count = 0
        index = 0
        
        while True:
            if index < len(arr) and current_num == arr[index]:
                index += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return current_num
            current_num += 1