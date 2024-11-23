import matplotlib.pyplot as plt
import numpy as np
import math
xlist=np.linspace(-10,10,100)
sinlist=[]
for i in xlist:
    sinlist.append(math.sin(i))
plt.subplot(2,1,1)
plt.plot(xlist,sinlist)
plt.title("Sine Curve")
coslist=[]
for i in xlist:
    coslist.append(math.cos(i))
plt.subplot(2,1,2)
plt.plot(xlist,coslist)
plt.title("Cosine Curve")
plt.show()