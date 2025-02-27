def swap_numbers():
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))
    a, b = b, a  # Swapping
    print(f"Swapped values: a = {a}, b = {b}")

swap_numbers()