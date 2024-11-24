import matplotlib.pyplot as plt
f=open("A9Q1_file.txt","r")
text=f.read()
name=[]
bill=[]
text_list=text.split()

for i in range(len(text_list)):
    if(i%2==0):
        name.append(text_list[i])
    else:
        bill.append(int(text_list[i]))

plt.bar(name,bill)
plt.title("Monthly Electric Consumption")
plt.xlabel("Name")
plt.ylabel("Bill")
plt.show()