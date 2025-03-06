def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage
arr = [1, 2, 4, 5, 6]
n = 6  # Last number in sequence
print(find_missing_number(arr, n))