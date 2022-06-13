import matplotlib.pyplot as plt
import numpy as np

x = np.array(['a', 'b', 'c', 'd', 'e'])
y = np.array([2, 5, 6, 7, 9])

# plt.bar(x, y)
# plt.barh(x, y)
# plt.bar(x, y, color='black', width=0.5)
plt.barh(x, y, color='black', height=0.2)
plt.show()
