import numpy as np
import sympy as sp
from scipy.interpolate import lagrange

def lagrange_interpolation(x_vals, y_vals, x_target):
    poly = lagrange(x_vals, y_vals)
    return poly(x_target), poly

def error_bound(n, x_vals, x_target):
   
    factorial_term = np.math.factorial(n+1)
    product_term = np.prod([abs(x_target - x) for x in x_vals])
    error = product_term / factorial_term
    return error


x_values = np.array([0.698, 0.733, 0.768, 0.803])
y_values = np.array([0.7661, 0.7432, 0.7193, 0.6946])


x_target = 0.750


for degree in range(1, 5):
    approx, poly = lagrange_interpolation(x_values[:degree+1], y_values[:degree+1], x_target)
    error = error_bound(degree, x_values[:degree+1], x_target)
    print(f"Degree {degree} Lagrange interpolation: {approx:.6f}, Error bound: {error:.6f}")
