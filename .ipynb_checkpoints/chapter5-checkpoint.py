import numpy as np

# ---- Poisson process simulation ----

n = 50
lambd = 10

# draw n samples from Expo(lambda)
samples = np.random.exponential(lambd, (n))

# perform a cumulative sum of the samples
arrival_times = np.cumsum(samples)
print(arrival_times)
