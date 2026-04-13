import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()
fig, axs = plt.subplots(2, 2)
x = np.arange(0, 10)

for i in range(10):
    axs[0, 0].clear()
    axs[0, 1].clear()
    axs[1, 0].clear()
    axs[1, 1].clear()

    y = np.random.randint(1, 50, size=10)

    axs[0, 0].plot(x, y)
    axs[0, 1].plot(x, y**2)
    axs[1, 0].plot(x, np.sqrt(y))
    axs[1, 1].plot(x, np.log(y))

    plt.pause(0.5)

plt.ioff()
plt.show()