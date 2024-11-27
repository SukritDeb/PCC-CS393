import csv
import matplotlib.pyplot as plt
f=open("./files/A9Q2.csv","w",newline='')
data=csv.writer(f)
data.writerow(["Student Name","DSA","Python","CO","Maths","Electronics","Average"])
num=int(input("Enter no of data: "))
for i in range(num):
    name=input("Enter the name: ")
    dsa=float(input("Enter the marks of DSA: "))
    python=float(input("Enter the marks of Python: "))
    co=float(input("Enter the marks of CO: "))
    maths=float(input("Enter the marks of Maths: "))
    electronics=float(input("Enter the marks of electronics: "))
    avg=(dsa+python+co+maths+electronics)/5
    list1=[name,dsa,python,co,maths,electronics,avg]
    data.writerow(list1)
f.close()
f2=open("./files/A9Q2.csv","r")
name=[]
avg=[]
readdata=[]
main=csv.reader(f2)
for i in main:
    readdata.append(i)
for row in range(1,len(readdata)):
    name.append(readdata[row][0])
    avg.append(float(readdata[row][6]))
plt.bar(name,avg)
plt.xlabel("Name")
plt.ylabel("Average Marks")
plt.title("Result")
plt.show()
    
f2.close()
