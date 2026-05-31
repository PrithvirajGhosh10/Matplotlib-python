import matplotlib.pyplot as plt
import numpy as np

# scatter graph = Show the relationship between two variables
#                 helps to identify a correlation (+,-,None)
#                 Example:Study hours vs. Test score

x1=[0,1,1,2,3,4,5,6,7,7,8] #hours studies
y1=[55,60,65,62,68,70,75,78,82,85,87] #grades

x2=[0,1,2,2,3,4,5,6,7,8,8] #hours studies
y2=[50,58,65,70,71,78,83,88,92,95,97] #grades

plt.scatter(x1,y1,color="skyblue",
            alpha=0.8, 
            s=200,
            label="class a")

plt.scatter(x2,y2,color="red",
            alpha=0.8, 
            s=200,label="class a")

plt.title("Test Scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")

plt.legend() #for label
plt.show()