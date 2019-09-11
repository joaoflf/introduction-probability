import numpy as np

# ---- Card Matching Problem ----
# Calculate the expected cards matched (deMontmort)
n = 100
results = []
for i in range(104):
    # sum number of times a random array of size n matches a range 1,2,..n
    # append each simulation to results
    results.append(int(np.sum(np.arange(n) == np.random.choice(n, n))))

# Print the mean or Expectancy
print(np.mean(np.array(results)))

# ---- Birthday problem ----
# Calculate the expected number of distinct birthdays in a group of k people
k = 20
results = []
for i in range(104):
    # Get unique birthdays from random sample of range 1..365 with replacement
    results.append(len(np.unique(np.random.choice(365, k, replace=True))))

# Print the mean or Expectancy
print(np.mean(np.array(results)))
