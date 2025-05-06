import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../csv_files/PastHires.csv")

df2 = df[['Previous employers','Hired']][5:11]

print(df2)

degree_counts = df2['Previous employers'].value_counts()

degree_counts.plot(kind='hist')
plt.show()