import matplotlib.pyplot as plt
import numpy as np

# scatter graph = Show the relationship between two variables
#                 helps to identify a correlation (+,-,None)
#                 Example:Study hours vs. Test score

x=[0,1,1,2,3,4,5,6,7,7,8] #hours studies
y=[55,60,65,62,68,70,75,78,82,85,87] #grades
plt.scatter(x,y,color="skyblue",alpha=0.8, s=200)#alpha is transperancy  #s=size
plt.title("Test Scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")
plt.show()