n=int(input("Enter the no of inputs: "))
if(n>=2):
    largest=float('-inf')
    secondlargest=float('-inf')
    for i in range(n):
        a=int(input(f"Enter the number {i+1}: "))
        if(a>largest):
            secondlargest=largest
            largest=a
        if(a>secondlargest and a!=largest):
            secondlargest=a
    if(secondlargest!=float('-inf')):
        print("Second largest = ",secondlargest)
    else:
        print("No second largest number exist")
