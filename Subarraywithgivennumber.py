def subarray_with_given_sum(arr, target):
    start, curr_sum = 0, 0
    
    for end in range(len(arr)):
        curr_sum += arr[end]
        
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1
        
        if curr_sum == target:
            return arr[start:end+1]
    
    return -1

# Example usage
arr = [1, 4, 20, 3, 10, 5]
target = 33
print(subarray_with_given_sum(arr, target))