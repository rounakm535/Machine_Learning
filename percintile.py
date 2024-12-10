import numpy
import matplotlib.pyplot as plt


data = [12, 14, 18, 16, 20]

p_25 = numpy.percentile(data, 25)

p_50 = numpy.percentile(data, 50)

p_75 = numpy.percentile(data, 75)

print(f"The 25th percentile is: {p_25}")
print(f"The 50th percentile is: {p_50}")
print(f"The 75th percentile is: {p_75}")

plt.boxplot(data)
plt.title("Boxplot with Percentile")
plt.xlabel("Data")
plt.ylabel("Values")
plt.show()
