import numpy as np
import matplotlib.pylab as plt

def signmoid_function(x):
	return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = signmoid_function(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1);
plt.show()
