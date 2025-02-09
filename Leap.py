def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
year = int(input("Enter a year: "))
print("Leap Year:", is_leap_year(year))