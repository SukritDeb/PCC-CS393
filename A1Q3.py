n = int(input("Enter a number: "))
r = int(str(n)[::-1])
print("Reversed number:", r)
if r % 2 == 0:
    print("The reversed number is even.")
else:
    print("The reversed number is odd.")