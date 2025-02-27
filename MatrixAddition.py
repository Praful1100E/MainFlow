def matrix_addition():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter elements for first matrix:")
    matrix1 = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

    print("Enter elements for second matrix:")
    matrix2 = [[int(input(f"Element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

    # Adding matrices
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

    print("Resultant Matrix:")
    for row in result:
        print(row)

matrix_addition()