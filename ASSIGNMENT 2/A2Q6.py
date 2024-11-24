n=int(input("Enter the row no: "))
for i in range(n):
    print((" "*i)+("*"*(2*n-1-2*i))+(" "*i))
