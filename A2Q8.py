def count(num):
    count=0
    while(num!=0):
        num=num//10
        count+=1
    return count
def sumofdigit(num):
    sum=0
    for i in range(count(num)):
        sum=sum+(num%10)
        num=num//10
    return sum
n=int(input("Enter your number: "))
while(count(n)!=1):
    n=sumofdigit(n)
if(n==1):
    print("Magic number...")
else:
    print("Not a magic number...")