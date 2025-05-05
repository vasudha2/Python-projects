# Input for first matrix
rows1 = int(input("Enter rows for first matrix: "))
columns1 = int(input("Enter columns for first matrix: "))
matrix1 = []
for i in range(rows1):
    d = []
    for j in range(columns1):
        v = int(input(f"Enter value for matrix1[{i}][{j}]: "))
        d.append(v)
    matrix1.append(d)

# Input for second matrix
rows2 = int(input("Enter rows for second matrix: "))
columns2 = int(input("Enter columns for second matrix: "))
matrix2 = []
for i in range(rows2):
    d = []
    for j in range(columns2):
        v = int(input(f"Enter value for matrix2[{i}][{j}]: "))
        d.append(v)
    matrix2.append(d)

# Check if matrices can be added
if rows1 == rows2 and columns1 == columns2:
    addition = []
    for i in range(rows1):
        d = []
        for j in range(columns1):
            v = matrix1[i][j] + matrix2[i][j]
            d.append(v)
        addition.append(d)

    print("Matrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Addition:", addition)
else:
    print("Matrices have different dimensions and cannot be added.")
