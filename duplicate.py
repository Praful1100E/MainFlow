from collections import Counter

def find_duplicates(lst):
    counter = Counter(lst)
    return [key for key, value in counter.items() if value > 1]

# Example usage
lst = [1, 2, 3, 4, 2, 3, 5, 6, 1]
print(find_duplicates(lst))