def check_substring():
    main_string = input("Enter the main string: ")
    sub_string = input("Enter the substring: ")
    if sub_string in main_string:
        print("True")
    else:
        print("False")

check_substring()