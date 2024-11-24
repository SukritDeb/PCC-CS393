p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
t = int(input("Enter the time period (in years): "))
s = (p * r * t) / 100
t1 = p + s
a = p * (1 + r / 100) ** t
c = a - p
t2 = p + c
print("Simple Interest:", s)
print("Total Amount (Simple Interest):", t1)
print("Compound Interest:", c)
print("Total Amount (Compound Interest):", t2)