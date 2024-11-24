total_marks=int(input("Enter the marks in each test: "))
marks1=int(input("Enter the marks in subject 1: "))
marks2=int(input("Enter the marks in subject 2: "))
marks3=int(input("Enter the marks in subject 3: "))
marks4=int(input("Enter the marks in subject 4: "))
marks5=int(input("Enter the marks in subject 5: "))
percentage=((marks1+marks2+marks3+marks4+marks5)/(total_marks*5))*100
print(f"Percentage: {percentage}%")
if(percentage>90 and percentage<100):
    grade="O"
elif(percentage>80):
    grade="A+"
elif(percentage>70):
    grade="A"
elif(percentage>60):
    grade="B"
elif(percentage>50):
    grade="C"
elif(percentage>40):
    grade="D"
elif(percentage>33):
    grade="E"
else:
    grade="F"
print(f"The grade is: {grade}")