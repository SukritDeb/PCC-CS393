import matplotlib.pyplot as plt
import random
month=["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
rent=[]
for i in range(12):
    rent.append(random.randint(100,1000))
print("1) line graph 2)Bar graph 3)Pie chart")
choice=int(input("Enter the choice: "))
if(choice==1):
    plt.plot(month,rent)
    plt.title("Line Graph")
    plt.xlabel("Month")
    plt.ylabel("Rent")

elif(choice==2):
    plt.bar(month,rent)
    plt.title("Bar Graph")
    plt.xlabel("Month")
    plt.ylabel("Rent")

elif(choice==3):
    
    plt.pie(rent,labels=month,autopct='%1.1f%%')

plt.show()