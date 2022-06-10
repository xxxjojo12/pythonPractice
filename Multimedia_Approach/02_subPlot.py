import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 10, 30, 255, 100, 40, 200, 1])
y = np.array([0, 100, 2, 50, 15, 190, 5, 255])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title('1st')

x = np.array([0, 10, 15, 1])
y = np.array([10, 15, 1, 10])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title('2nd')

# Super Title
plt.suptitle('Title')

plt.show()
