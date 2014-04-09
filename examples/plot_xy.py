
import sys
sys.path.append("../")

import mpl_header
import matplotlib.pyplot as plt

import numpy as np


def gaussian(x, a=1.0, b=1.0, c=1.0, d=0.0):
    """ Normal distribution

    http://en.wikipedia.org/wiki/Gaussian_function

    """

    return a*np.exp(-(x-b)**2/(2*c**2))+d


def lorentzian(x):
    """ Lorentz(ian) function

    http://en.wikipedia.org/wiki/Cauchy_distribution

    """

    a = 0.9
    b = -2.0

    return 1.0/(np.pi*a*(1+((x-b)/a)**2))



x_list = np.arange(-10, 10, 0.1)
y_gauss = [gaussian(x) for x in x_list]
y_lortenz = [lorentzian(x) for x in x_list]


plt.title('Distributions')

plt.plot(x_list, y_gauss, label='Gauss')
plt.plot(x_list, y_lortenz, label='Lorentz')

plt.legend(loc='upper left')

plt.ylabel('Probability [$p(x)$]')
plt.xlabel('Position [$x$]')

plt.savefig('figure_xy.png')

