def is_pythagorean_triplet(a, b, c):
    x, y, z = sorted([a, b, c])
    return x*x + y*y == z*z

# Example usage
print(is_pythagorean_triplet(3, 4, 5))  # True
print(is_pythagorean_triplet(5, 12, 13))  # True
print(is_pythagorean_triplet(1, 2, 3))  # False