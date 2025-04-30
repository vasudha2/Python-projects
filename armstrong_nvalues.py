n = int(input("Enter a number: "))
for i in range(n+1):
    count=len(str(i))
    sum=0
    temp=i
    while temp > 0:
        digit = temp % 10
        sum += digit ** count 
        temp = temp // 10
    if(sum==i):
        print(i)

