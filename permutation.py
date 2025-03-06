from itertools import permutations

def find_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example usage
s = "abc"
print(find_permutations(s))