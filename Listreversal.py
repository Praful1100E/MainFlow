def reverse_list(lst):
    return lst[::-1]


lst = list(map(int, input("Enter list elements: ").split()))
print(reverse_list(lst))