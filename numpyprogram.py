#we have to install pandas first
import numpy as np
import matplotlib.pyplot as plt

# Given doubling array
doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Create an array of integers from 1 to 10
one_to_ten = np.arange(1, 11)  # 1 through 10

# Create scatter plot
plt.scatter(one_to_ten, doubling_array)
plt.show()
