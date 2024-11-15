s=input("Enter the string: ")
lower=0
upper=0
for i in s:
    if(i.isupper()):
        upper+=1
    elif(i.islower()):
        lower+=1
print(f"No of upper case is {upper} and no of lower case is {lower}")