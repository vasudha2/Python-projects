n=int(input("enter number"))
a=0
b=1
for i in range(n):
    temp=a
    print(a,end=" ")
    a=a+b
    b=temp
    
