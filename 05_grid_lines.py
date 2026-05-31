import matplotlib.pyplot as plt
import numpy as np
#grid() = helps make plots easier to read by adding referance lines.
x=[1,2,3,4,5]
y=[5,10,15,20,25]

#plt.grid()                                            #with no argument
#plt.grid(axis="x")                                    #only x axis
#plt.grid(axis="y")                                    #only y axis
# plt.grid(linewidth=3,color="blue", linestyle="dashed")
plt.grid(linewidth=3,color="blue", linestyle="dashdot")



plt.plot(x,y)
plt.show()