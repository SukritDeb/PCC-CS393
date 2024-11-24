def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            return 0
    return 1
a=int(input("Enter the number: "))
b=int(a**0.5)
if(prime(b)):
    print("Square root is prime")
else:
    print("Square root is not prime")