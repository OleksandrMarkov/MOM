import numpy as np
A = [[4, 6, 2],
     [3, 4, 1],
     [2, 8, 13]]

s = [9, 7, 2]

r = np.linalg.solve(A, s)

# solve linear Ar = s
# results: [ 3.  -0.5  0. ]
