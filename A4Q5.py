l=eval(input("Enter the list: "))
m=int(input("Enter the first index:"))
n=int(input("Enter the last index: "))
flag=0
for i in range(m,n+1):
    if(m>0 and n>0 and m<len(l) and n<len(l) and m<n):
        max=l[m]
        min=l[m]
        for i in range(m,n+1):
            if(l[i]<min):
                min=l[i]
            if(l[i]>max):
                max=l[i]
        print(f"Minimum is {min} and Maximum is {max}")
    else:
         flag=1
if(flag==1):
    print("Wrong Index")
            
