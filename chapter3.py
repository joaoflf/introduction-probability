import numpy as np
from scipy.stats import binom

# binomial distribution PMF, CDF and sampling
bin = binom(5, 0.2)

print(bin.pmf(3))
print(bin.cdf(3))
print(bin.rvs(7))

# sample from finite set with corresponding probabilities with replacement
set = [0, 1, 5, 10]
probabilities = [0.25, 0.5, 0.1, 0.15]
samples = np.random.choice(set, 100, replace=True, p=probabilities)
print(samples)
