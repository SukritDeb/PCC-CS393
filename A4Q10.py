arr=eval(input("Enter the list: "))
mean=sum(arr)/len(arr)
var=0
for i in arr:
    var=var+(i-mean)**2
varience=var/len(arr)
sd=varience**(0.5)
print("Mean = ",mean)
print("Varience = ",varience)
print("Standard Deviation = ",sd)