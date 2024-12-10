import pandas

data = [12, 18, 20, 25, 44, 36, 44, 46, 44, 16, 24]

mean = sum(data) / len(data)

print(f"The mean value is {mean}")

s_data = sorted(data)
n = len(s_data)

median = (s_data[n // 2] + s_data[(n-1) // 2]) / 2

print(f"The median value is {median}")

from statistics import mode

mode_value = mode(data)

print(f"The mode value is {mode_value}")
