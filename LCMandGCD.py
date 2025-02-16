import math

def gcd_lcm(a, b):
    gcd_value = math.gcd(a, b)
    lcm_value = (a * b) // gcd_value
    return lcm_value, gcd_value

# Example usage
a, b = map(int, input("Enter two numbers: ").split())
print(gcd_lcm(a, b))