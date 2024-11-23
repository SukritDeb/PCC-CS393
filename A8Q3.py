import matplotlib.pyplot as plt
import random
x=[]
y=[]
for i in range(0,30):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
plt.scatter(x,y)
plt.show()