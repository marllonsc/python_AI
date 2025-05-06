import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

incomes = np.random.normal(27000,15000,10000)

print(np.mean(incomes))
#plt.hist(incomes,50)
#plt.show()

print(np.median(incomes))

incomes = np.append(incomes,[1000000000])

print(np.median(incomes))
print(np.mean(incomes))

ages = np.random.randint(18, high=90, size=500)
print(ages)

print(stats.mode(ages))