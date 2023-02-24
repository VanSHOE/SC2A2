import numpy as np
import matplotlib.pyplot as plt
import random
import time
from alive_progress import alive_bar

random.seed(time.time())

b = 2
a = -b


def random_walk(start: int, timesteps: int) -> int:
    cur = start
    for _ in range(timesteps):
        cur += random.choice([-1, 1])

    return cur


ITERATIONS = 100000

# a
probs = [0] * 100
with alive_bar(100) as bar:
    for N in range(1, 101):
        reached_origin = 0
        for _ in range(ITERATIONS):
            reached_origin += random_walk(a, N) == 0

        prob = reached_origin / ITERATIONS
        probs[N - 1] = prob
        bar()

plt.plot(range(1, 101), probs)
plt.show()

# b
probs = [0] * 100
with alive_bar(100) as bar:
    # two drunk people, find if they are at equal thing after N
    for N in range(1, 101):
        reached_each_other = 0
        for _ in range(ITERATIONS):
            reached_each_other += random_walk(a, N) == random_walk(b, N)

        prob = reached_each_other / ITERATIONS
        probs[N - 1] = prob
        bar()

plt.plot(range(1, 101), probs, c='r')
plt.show()

# c
# mean displacement
means = [0] * 100
with alive_bar(100) as bar:
    for N in range(1, 101):
        displacements = []
        for _ in range(ITERATIONS):
            displacements.append(random_walk(0, N))

        mean = np.mean(displacements)
        means[N - 1] = mean
        bar()

plt.plot(range(1, 101), means, c='g')
plt.show()
