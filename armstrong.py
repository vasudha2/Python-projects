#a number is said to be armstrong when the power of its length sum is equal to the given number example 153 1^3+5^3+3^3=153 so its an armstrong number
n = int(input("Enter a number: "))
count = len(str(n))  
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** count 
    temp = temp // 10

if sum == n:
    print("%d Armstrong number"%n)
else:
    print("Not an Armstrong number")
