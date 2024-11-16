arr=eval(input("Enter the list: "))
i=0
j=len(arr)-1
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
while(i<j):
    swap(arr,i,j)
    i+=1
    j-=1
print(arr)
