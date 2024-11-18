def binarysearch(arr,ele,start,end):
    if(start<=end):
        mid=(start+end)//2
        if(arr[mid]==ele):
            return mid
        elif(arr[mid]<ele):
            return binarysearch(arr,ele,mid+1,end)
        elif(arr[mid]>ele):
            return binarysearch(arr,ele,start,mid-1)
    else:
        return -1
arr=eval(input("Enter the sorted array: "))
ele=int(input("Enter the element: "))
index=binarysearch(arr,ele,0,len(arr)-1)
if(index==-1):
    print("Element not found")
else:
    print("Element found at index: ",index)