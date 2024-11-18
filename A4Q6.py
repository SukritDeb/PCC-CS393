l=eval(input("Enter the list: "))
result=[]
for i in l:
    if(l.count(i)==1):
        result.append(i)
for i in l:
    if(l.count(i)>1):
        result.append(i)
print(result)
