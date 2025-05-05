#input for 1st matrix

rows1=int(input("enter no.of rows: "))
columns1=int(input("enter no.of columns"))
matrix1=[]
for i in range(rows1):
    dup=[]
    for j in range(columns1):
        v=int(input(f"enter strings in format of {[i]} {[j]}: "))
        dup.append(v)
    matrix1.append(dup)
rows2=int(input("enter no.of rows: "))
columns2=int(input("enter no.of columns"))
matrix2=[]
for i in range(rows1):
    dup=[]
    for j in range(columns1):
        v=int(input(f"enter strings in format of {[i]} {[j]}: "))
        dup.append(v)
    matrix2.append(dup)
if(rows1!=columns2):
    print("they should be equal")
else:
    multiplication=[]
    for i in range(rows1):
        dup=[]
        for j in range(columns2):
            dup.append(0)
        multiplication.append(dup)
    for i in range(rows1):
        for j in range(columns2):
            for k in range(columns1):
                multiplication[i][j]+=matrix1[i][k]*matrix2[k][j]
print(multiplication)
