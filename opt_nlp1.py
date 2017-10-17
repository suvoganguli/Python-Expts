from scipy.optimize import minimize
import numpy as np


def f(x):
    return np.square(x) + 1


# def cons(x):
#     a = 3
#     return x - a


x0 = np.array([-3])

sol = minimize(f,x0)
print(sol)


