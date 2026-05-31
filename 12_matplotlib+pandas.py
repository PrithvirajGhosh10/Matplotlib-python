import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")
type_count=df["type1"].value_counts(ascending=True)
plt.barh(type_count.index,type_count.values, color="lightgreen",edgecolor="black")

plt.title("No of pokemon by primary count")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()

plt.show()
