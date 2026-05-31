import matplotlib.pyplot as plt
import numpy as np

# Bar chart= Circular chart divided into slices to show pergentage of the total.
#             good for visualizing distribution among categories.
categories=["Freshmen","Sophomores","Juniors","Seniors"]
values=np.array([300,250,275,225])
plt.pie(values, labels= categories,autopct="%1f")#cateroris+pargentages show (autopct= auto parcentage)  #%1f to format a construction
plt.show()