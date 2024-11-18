def minmax(arr):
    if(len(arr)>1):
        min_index=0
        max_index=0
        result=[]
        for i in range(1,len(arr)):
            if(min>arr[i]):
                min_index=i
            if(max<arr[i]):
               
                max_index=i
        result.append(min_index)
        result.append(max_index)
        return result
arr=eval(input("Enter the list: "))
r=minmax(arr)
print(f"Minimnum element is {arr[r[0]]} at index {r[0]} and Maximum element is {arr[r[1]]} at index {r[1]}")
