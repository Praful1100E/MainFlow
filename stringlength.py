def string_length(s):
    count = 0
    for char in s:
        count += 1 
    return count

text = input("Enter a string: ")
print("Length of the string:", string_length(text))