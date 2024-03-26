import numpy as np

def f(x):
    return np.sin(x) / x

for i in range(-5,5):
    j = 1 ** i
    print(f(j))