import numpy as np
from scipy.interpolate import CubicHermiteSpline

# 時間、距離、速度數據
T = np.array([0, 3, 5, 8, 13])
D = np.array([0, 200, 375, 620, 990])
V = np.array([75, 77, 80, 74, 72])


interp_position = CubicHermiteSpline(T, D, V)  # 插值距離
interp_speed = CubicHermiteSpline(T, V, V)    # 插值速度

# 預測 t = 10 時的距離和速度
t = 10
predicted_position = interp_position(t)
predicted_speed = interp_speed(t)

print(f"Predicted position at t = 10 seconds: {predicted_position:.2f} feet")
print(f"Predicted speed at t = 10 seconds: {predicted_speed:.2f} feet per second")
