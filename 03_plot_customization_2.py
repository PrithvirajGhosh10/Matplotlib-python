import matplotlib.pyplot as plt
import numpy as np
x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([17,23,38,5])
y3=np.array([13,15,20,5])#3rd line

line_style=dict(marker=".", #creating dictionaries
                markersize=30,
                markerfacecolor="#0D8B9E",
                markeredgecolor="#A6D36B", 
                linestyle="solid",                                                                  
                linewidth=3,                                                                         
                )
plt.plot(x,y1,color="blue",**line_style)#unpack dicgt
plt.plot(x,y2,color="green",**line_style)                 #changing colour
plt.plot(x,y3,color="red",**line_style)
plt.show()