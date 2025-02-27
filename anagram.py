def check_anagram():
    str1 = input("Enter first string: ").replace(" ", "").lower()
    str2 = input("Enter second string: ").replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        print("True")  # Strings are anagrams
    else:
        print("False")  # Strings are not anagrams

check_anagram()