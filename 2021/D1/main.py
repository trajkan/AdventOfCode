import numpy as np


# with open('input.txt') as f:
#     contents = f.read()

data = np.loadtxt('input.txt')

diff = np.diff(data)

print(diff)

increasing_nbr = len(diff > 0 )
print(increasing_nbr)
print(len(data))


