n=int(input("enter no.of elements you need"))
matrix=[]
for i in range(n):
    v=int(input("enter numbers: "))
    matrix.append(v)
print(matrix)
unique=[]
for num in matrix:
    if num in unique:
        unique.append(num)
print(unique)
