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



#creating using numpy
import numpy as np
a=np.array([1,2,3],[4,5,6])
print(a)
print(a.ndim) # prints dimension of a
