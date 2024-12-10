import matplotlib.pyplot as plt
import numpy

data = numpy.random.normal(0, 1, 100)

plt.hist(data, bins=30, edgecolor= "black")
plt.title("Histogram of Dataset Distribution.")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

mean_val = numpy.mean(data)
median_val = numpy.median(data)
std_dev = numpy.std(data)

print(f"Mean value : {mean_val}")
print(f"Median value : {median_val}")
print(f"Standard Deviation : {std_dev}")
