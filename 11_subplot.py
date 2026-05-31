import matplotlib.pyplot as plt
import numpy as np

# Figure = the entire canvas
# Ax = A single plot(subplot)
x=np.array([1,2,3,4,5])
figure,axes=plt.subplots(2,2) #2rows 2columns

axes[0,0].plot(x,x*2,color="red") #for first row and first column
axes[0,0].set_title("x*2") #giving it a title

axes[0,1].plot(x,x**2,color="blue") #for first row and second column
axes[0,1].set_title("x**2") #giving it a title

axes[1,0].plot(x,x**3,color="green") #for second row and first column
axes[1,0].set_title("x**3") #giving it a title

axes[1,1].plot(x,x**4,color="purple") #for second row and second column
axes[1,1].set_title("x**4") #giving it a title

plt.show()
