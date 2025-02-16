# Standard Deviation and Variance
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)

plt.hist(incomes, 50, color='green', edgecolor='black')

plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")

plt.show()

incomes.std()

incomes.size

incomes.var()

# iterate over incomes

Experiment
with different parameters on the normal function, and see what effect it has on the shape of the distribution.How does that new shape relate to the standard deviation and variance?
