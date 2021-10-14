import numpy as np

def calc_grid(n):
    def nearest_square(num):
        num1 = np.floor(np.sqrt(num))**2
        return np.sqrt(num1)

    n_rows = int(nearest_square(n))
    n_cols = n_rows

    while True:
        if n_cols * n_rows < n:
            n_cols += 1
        else:
            break
    return n_rows, n_cols