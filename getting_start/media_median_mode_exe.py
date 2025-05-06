import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)

plt.hist(incomes, 50000)
plt.show()


print(np.median(incomes))