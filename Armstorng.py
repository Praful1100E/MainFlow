def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n
num = int(input("Enter a number: "))
print("Armstrong Number:", is_armstrong(num))