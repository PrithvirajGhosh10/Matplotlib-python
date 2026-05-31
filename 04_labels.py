import matplotlib.pyplot as plt
import numpy as np
x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([17,23,38,5])
y3=np.array([13,15,20,5])

plt.title("class size", fontsize=25,         #label title on top
                        family="arial",
                        fontweight="bold",
                        color="blue")

plt.xlabel("Year",fontsize=20,family="arial",fontweight="bold",color="yellow")                    #lebel on x axis
plt.ylabel("Students",fontsize=20,family="arial",fontweight="bold",color="yellow")                #lebel on Y axis

plt.tick_params(axis="both" , colors="purple") #the scale (nos./marking) change


plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.xticks(x)#to get the original input not in point
plt.show()