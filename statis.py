values = []
while True:
    number = input("Enter a number (or type 'done' to finish): ")
    if number.lower() == 'done':
        break
    try:
        values.append(float(number))
    except ValueError:
        print("Please enter a valid number.")
if len(values) == 0:
    print("No numbers were entered.")
else:
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    standard_deviation = variance ** 0.5
    print("Arithmetic Mean:", mean)
    print("Variance:", variance)
    print("Standard Deviation:", standard_deviation)