import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 10, 30, 255, 100, 40, 200, 1])
y = np.array([0, 100, 2, 50, 15, 190, 5, 255])


font1 = {'family': 'Times New Roman', 'color': '#293056', 'size': 13}

# plt.plot(y, 'D:r')
# plt.plot(y, 'D--b')
# plt.plot(y, marker='D', ms=20)

# marker encounter, marker face color
# plt.plot(y, marker='D', ms=15, mec='y', mfc='hotpink')

plt.plot(y, ls='dotted', c='g', linewidth='10')
plt.plot(x)

# Naming labels
plt.xlabel('xlabel')
plt.ylabel('ylabel')

# Naming plot and location of the title
plt.title('Learning plot', fontdict=font1, loc='right')

# grid line for x
# plt.grid(axis='x')

# gridline 꾸미기
plt.grid(color='y', linestyle='--', linewidth=0.3)

plt.show()
