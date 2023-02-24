import numpy as np
import matplotlib.pyplot as plt
import random
import time

random.seed(time.time())


def f(x):
    return x * x * np.cos(x)


# monte carlo integration
def monte_carlo(f, N):
    x = np.random.uniform(0, 1, N)

    x = np.array(sorted(x)) * np.pi - np.pi / 2

    y = f(x).astype(np.float64)

    return (np.sum(y) / N) * np.pi


# a
print(monte_carlo(f, 100000))

# b
# x = [1, 1000, 2000, ... , 100000]
x = np.arange(1000, 100000 + 1, 1000)
x = [1] + list(x)
x = np.array(x)
print(x)

# plot
y = np.array([monte_carlo(f, i) for i in x])
plt.plot(x, y)
plt.show()
