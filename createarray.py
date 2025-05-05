rows = int(input("enter rows"))
columns = int(input("enter columns"))
matrix = []
for i in range(rows):
    dup_matrix = []
    for j in range(columns):
        v = int(input())
        dup_matrix.append(v)
    matrix.append(dup_matrix)
print(matrix)
