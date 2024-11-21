def isPrime(num):
    if(num<2):
        return False
    prime=True
    for i in range(2,num):
        if(num%i==0):
            prime=False
    return prime
n=int(input("Enter the number: "))
sum=0
count=0
num=0
while(count!=n):
    num=num+1
    if(isPrime(num)):
        sum=sum+num
        print(sum)
        count=count+1
