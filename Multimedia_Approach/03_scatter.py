import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 4, 5, 6])
y = np.array([2, 5, 6, 7, 9])
colors = ['red', 'black', 'blue', 'yellow', 'cyan']

plt.scatter(x, y, c=colors)

# plt.scatter(x, y)
# plt.show()

x = np.array([11, 13, 14, 51, 61])
y = np.array([21, 51, 16, 17, 91])

sizes = [20, 20, 20, 20, 200]

plt.scatter(x, y, s=sizes, alpha = 0.5)
plt.show()
