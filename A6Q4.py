def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def bubblesort(arr):
    for i in range(len(arr)):
        isSort=True
        for j in range(0,len(arr)-1):
            if(arr[j]>arr[j+1]):
                swap(arr,j,j+1)
                isSort=False
        if(isSort):
            break

arr=eval(input("Enter the list: "))
bubblesort(arr)
print(arr)