# from scipy.special import binom
import numpy as np

# ---- de Montmort's problem ----
n = 100
win = 0
for i in range(10**4):
    # add when a random array of size n matches at least 1 element in a range n
    win += (np.sum(np.arange(n) == np.random.choice(n, n)) > 0)

# this should be close to e
print(win/10**4)

# ---- Birthday problem ----
k = 59
prob = 1 - np.prod(np.arange(365 - k + 1, 366), dtype=np.float64) / (365**k)
print(prob)
