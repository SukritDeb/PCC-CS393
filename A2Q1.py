a=int(input("Enter the no of product bought: "))
if(a<10 and a>=0):
    rate=120
elif(a>=10 and a<=99):
    rate=100
elif(a>=100):
    rate=70
else:
    rate=0
if(rate==0):
    print("Invalid input")
else:
    price=rate*a
    print("Total cost: ",price)
