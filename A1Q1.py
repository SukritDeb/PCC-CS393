years = int(input("Enter the number of years: "))
days = years * 365
is_leap_year = (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)
if is_leap_year:
    days += years // 4 - years // 100 + years // 400
    print("Its's a Leap Year.")
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In", years, "years, there are:")
print(days, "days")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")