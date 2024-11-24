arr=eval(input("Enter the list: "))
search=int(input("Enter the element: "))
found=0
for i in range(len(arr)):
    if(arr[i]==search):
        print("present at position: ",i+1)
        found=1
if(found==0):
    print("Not Found.. ")
