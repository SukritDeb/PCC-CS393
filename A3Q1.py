s=input("Enter a string: ")
result=""
for i in s:
    if(i not in result and s.count(i)%2!=0):

        result=result+i
print(result)