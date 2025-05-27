import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {'A': [1, 2, 3, 4, 5],
        'B': [2, 4, 5, 4, 5],
        'C': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()