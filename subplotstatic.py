import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(0, 10)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, x)
axs[0, 1].plot(x, x**2)
axs[1, 0].plot(x, np.sqrt(x))
axs[1, 1].plot(x, np.log(x + 1))

plt.show()