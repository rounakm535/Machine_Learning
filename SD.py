import math

data = [12, 18, 14, 20, 98, 33, 35, 37, 1, 16]

mean = sum(data) / len(data)

var = sum((x - mean)**2 for x in data) / len(data)

std_deviation = math.sqrt(var)

print(f"The value of standard deviation is {std_deviation}")
