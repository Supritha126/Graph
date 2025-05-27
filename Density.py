import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = np.random.randn(1000)
sns.kdeplot(data)
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Density Plot")
plt.show()