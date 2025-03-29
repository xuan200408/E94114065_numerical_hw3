import numpy as np
from scipy.interpolate import KroghInterpolator
import scipy.optimize as opt

# 時間、距離、速度數據
T = np.array([0, 3, 5, 8, 13])
D = np.array([0, 200, 375, 620, 990])
V = np.array([75, 77, 80, 74, 72])


speed_limit_fps = 55 * 5280 / 3600


interp_speed = KroghInterpolator(T, V)


def speed_derivative(t):
    
    return interp_speed.derivatives(t)[1]


def speed_limit_exceed_time(t):
    return interp_speed(t) - speed_limit_fps


result = opt.root(speed_limit_exceed_time, 8)  # 初始猜測為 t = 8
if result.success:
    time_when_speed_exceeds = result.x[0]
    print(f"The car first exceeds the speed limit at t = {time_when_speed_exceeds:.2f} seconds.")
else:
    print("The car never exceeds the speed limit.")

