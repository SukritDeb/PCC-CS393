def count(num):
    count=0
    while(num!=0):
        num=num//10
        count+=1
    return count
def reverse(num):
    c=count(num)
    newnum=0
    for i in range(1,c+1):
        r=num%10
        newnum=newnum+r*(10**(c-i))
        num=num//10
    return newnum
n=int(input("Enter the number: "))
for i in range(1,n+1):
    if(reverse(i)==i):
        print(i)
    