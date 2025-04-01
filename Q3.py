import numpy as np
from scipy.interpolate import CubicHermiteSpline
import matplotlib.pyplot as plt

# 資料：時間 T (s)、位置 D (ft)、速度 V (ft/s)
T = np.array([0, 3, 5, 8, 13])
D = np.array([0, 200, 375, 620, 990])
V = np.array([75, 77, 80, 74, 72])  # feet/second

# 建立 Cubic Hermite 插值器
hermite_spline = CubicHermiteSpline(T, D, V)

# (a) 預測 t = 10 秒的距離與速度
t_eval = 10
position_at_10 = hermite_spline(t_eval)
speed_at_10 = hermite_spline.derivative()(t_eval)

print("=== (a) 預測 t = 10s 時的狀態 ===")
print(f"位置: {position_at_10:.2f} feet")
print(f"速度: {speed_at_10:.2f} ft/s")

# (b) 檢查是否超過 55 mi/h = 80.67 ft/s
t_fine = np.linspace(0, 13, 500)
speeds = hermite_spline.derivative()(t_fine)

exceeds_55mph = np.any(speeds > 80.67)
first_exceed_time = t_fine[speeds > 80.67][0] if exceeds_55mph else None

print("\n=== (b) 是否超過 55 mi/h? ===")
print(f"有超過: {exceeds_55mph}")
if exceeds_55mph:
    print(f"第一次超過的時間: {first_exceed_time:.2f} 秒")

# (c) 最大速度與時間
max_speed = np.max(speeds)
max_speed_time = t_fine[np.argmax(speeds)]

print("\n=== (c) 最大速度 ===")
print(f"最大速度: {max_speed:.2f} ft/s")
print(f"出現時間: {max_speed_time:.2f}秒")

