import numpy as np
import matplotlib.pyplot as plt


def nextNum(A, C, M, x):
    return (A * x + C) % M


# a
# x = 1 to 1000, plot I with this
x = np.arange(1, 1001)
I = np.zeros(1000)
I[0] = 1
for i in range(1, 1000):
    I[i] = nextNum(106, 1283, 6075, I[i - 1])

plt.scatter(x, I)
plt.show()

# b I_j + 1 vs I_j
plt.scatter(I[0:999], I[1:1000])
plt.show()

# In this plot we see that the points are not uniformly distributed. There are a lot of empty spaces and a lot of
# clusters. However, this technique is good enough to generate random numbers for generic purposes but not cryptographic
# purposes.

# c

# N = 1, 10, 50, ... 2000
N = [1, 10, 50]
N.extend(np.arange(100, 2001, 100))

y = []
for n in N:
    Isum = 1
    I = 1
    for i in range(1, n):
        I = nextNum(106, 1283, 6075, I)
        Isum += I

    Isum /= n
    y.append(Isum)

plt.scatter(N, y)
plt.show()
