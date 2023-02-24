import numpy as np
import matplotlib.pyplot as plt
import random
import time

random.seed(time.time())

N = 100000


def f(x):
    return x * x * np.cos(x)


# monte carlo integration
x = np.random.uniform(0, 1, N)
x = sorted(x) * np.pi - np.pi / 2
y = f(x).astype(np.float64)

sum = (np.sum(y) / N) * np.pi
print(sum)
