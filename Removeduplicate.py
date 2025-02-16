def remove_duplicates(lst):
    return list(set(lst))

lst = list(map(int, input("Enter list elements: ").split()))
print(remove_duplicates(lst)) 