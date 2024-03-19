import numpy as np

A = [[1, 1, 3],
     [1, 2, 4],
     [1, 1, 2]]
Ainv = np.linalg.inv(A)

# Output
# [[ 0. -1.  2.]
#  [-2.  1.  1.]
#  [ 1.  0. -1.]]
