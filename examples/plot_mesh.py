
import sys
sys.path.append("../")

import mpl_header
import matplotlib.pyplot as plt

import numpy as np

np.random.seed(500)

def gaussian(x, y, a=1.0, sigma_x=1.5, sigma_y=1.0, x_0=0.0, y_0=0.0):
    """ Gaussian Function

    http://en.wikipedia.org/wiki/Gaussian_function

    """
    return a*np.exp(-((x-x_0)**2/(2*sigma_x**2)+(y-y_0)**2/(2*sigma_y**2)))

# Data

X = np.arange(-3.0, 3.0, 0.1)
Y = np.arange(-3.0, 3.0, 0.1)

N = len(X)

Z = np.zeros((N, N))

for i in xrange(N):
    for j in xrange(N):
        Z[i,j] = gaussian(X[i], Y[j])


# Plot

extent = [X[0], X[-1], Y[0], Y[-1]]

im = plt.imshow(Z,
                interpolation='nearest',
                extent=extent,
                aspect='auto',
                origin='lower',
                cmap='Spectral')

plt.xlabel('$x$-direction')
plt.ylabel('$y$-direction')
plt.title('Gaussian')


plt.grid(False)

# Colorbar
cbar = plt.colorbar(im)
cbar.set_label('Propability [$p(x,y)$]', rotation=270)

plt.savefig('figure_mesh.png')


