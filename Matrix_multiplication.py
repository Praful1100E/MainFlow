def matrix_multiplication():
    # Taking input for matrix dimensions
    rows_A = int(input("Enter number of rows for matrix A: "))
    cols_A = int(input("Enter number of columns for matrix A: "))
    
    rows_B = cols_A
    cols_B = int(input("Enter number of columns for matrix B: "))

    print("Enter elements for matrix A:")
    A = [[int(input(f"A[{i}][{j}]: ")) for j in range(cols_A)] for i in range(rows_A)]

    print("Enter elements for matrix B:")
    B = [[int(input(f"B[{i}][{j}]: ")) for j in range(cols_B)] for i in range(rows_B)]

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    print("Resultant Matrix:")
    for row in result:
        print(row)

matrix_multiplication()