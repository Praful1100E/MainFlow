import heapq

def find_k_largest(lst, k):
    return heapq.nlargest(k, lst)

# Example usage
lst = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(find_k_largest(lst, k))