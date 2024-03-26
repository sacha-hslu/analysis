import numpy as np

def f(x):
    return x ** 2 - 1


a = - 1 / 2
b = 2

x = a - f(a) * (b - a) / (f(b) - f(a))

print(x)
print(f(a) * f(b))
print(1E-5)