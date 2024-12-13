l=eval(input("Enter the list: "))
l.sort()
size=len(l)
if(size%2==0):
    median=(l[(size//2)-1]+l[size//2])/2
else:
    median=l[(size-1)//2]
print("Median of the list: ",median)