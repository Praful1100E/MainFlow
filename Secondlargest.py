def find_second_largest():
    nums = list(map(int, input("Enter a list of integers separated by space: ").split()))
    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 2:
        print("No second largest element")
    else:
        unique_nums.sort(reverse=True)
        print("Second largest number:", unique_nums[1])

find_second_largest()