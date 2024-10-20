a=int(input("Enter the total no of cookies: "))
box=a//24
cookiesleftover=a%24
container=box//75
boxleftover=box%75
print("No of boxes requied: ",box)
print("No of container required: ",container)
print("Left over cookies: ",cookiesleftover)
print("left over boxes: ",boxleftover)