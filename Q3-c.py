import numpy as np


T = np.array([0, 3, 5, 8, 13])
V = np.array([75, 77, 80, 74, 72])

# 拉格朗日插值法
def lagrange_interpolation(x, x_data, y_data):
    n = len(x_data)
    result = 0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term = term * (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result


time_steps = np.linspace(0, 13, 1000) 
max_speed = None


for t in time_steps:
    speed = lagrange_interpolation(t, T, V)
    if max_speed is None or speed > max_speed:
        max_speed = speed


print(f"The predicted maximum speed of the car is {max_speed:.2f} feet per second.")
