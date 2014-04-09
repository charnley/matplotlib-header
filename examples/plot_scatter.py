
import sys
sys.path.append("../")

import mpl_header
import matplotlib.pyplot as plt

import numpy as np

np.random.seed(50)

# Fake Data
X = np.arange(-20.0, 0.0, 0.1)
Y1 = np.array([x+np.random.uniform(2,-2) for x in X])
Y2 = np.array([x+np.random.uniform(2,-2) for x in X])
X = np.array([x+np.random.uniform(2,-2) for x in X])


# Lines
lin = np.array([-100,100])
linp = lin + 2.0
linm = lin - 2.0
plt.plot(lin, lin, 'k-')
plt.plot(lin, linm, 'r--')
plt.plot(lin, linp, 'r--')


plt.plot(X, Y1, '.', label='Method 1')
plt.plot(X, Y2, '.', label='Method 2')

plt.legend(loc='upper left')

plt.ylim(-20, 0)
plt.xlim(-20, 0)


# Labels
plt.xlabel('Experimental [kcal/mol]')
plt.ylabel('Theoretical [kcal/mol]')


# Save the figure in different formats
plt.savefig('figure_scatter.png')
