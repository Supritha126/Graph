import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
data = np.random.normal(100, 20, 200)
plt.figure(figsize=(8, 6))
plt.boxplot(data)
plt.title('Boxplot Example')
plt.ylabel('Values')
plt.show()