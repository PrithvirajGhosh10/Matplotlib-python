import matplotlib.pyplot as plt
import numpy as np
x=np.array([2023,2024,2025,2026])
y=np.array([15,25,30,20])
plt.plot(x,y,marker=".", #marker mark the points 
             markersize=30,#markersize to increase or decrease the size of the marked point       #can be written as ms
             markerfacecolor="red",#show or change the colour of the marked point                 #can be written as mfc
             markeredgecolor="green", #edge of the marked point                                   #can be written as mec 
             #LINE CUSTOMIZATION
             #linestyle="dashed",                                                                 #to get the line dashed
             #linestyle="doted",                                                                  #to get the line dashed
             #linestyle="dashdot",                                                                #to get the line dashed
             #linestyle="none",                                                                   #to get no line
             linestyle="solid",                                                                   #to get nornal line
             linewidth=3,                                                                         #change the width of the line
             color="black")

plt.show()