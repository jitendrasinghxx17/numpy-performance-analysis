#Broadcasting: Scaling Arrays Without Extra Memory

import numpy as np

# Sample dataset
data = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40],
    [25, 35, 45],
    [30, 40, 50]
])

mean = data.mean(axis=0)
std = data.std(axis=0)

normalized_data = (data - mean) / std

print("Normalized Data:\n", normalized_data)
