l=eval(input("Enter the list 1 :"))
m=eval(input("Enter the list 2: "))
result=[]
if(len(l)==len(m)):
    for i in range(len(l)):
        result.append(l[i]+m[i])
    print("The result list: ",result)
else:
    print("The lists should be of same size..")