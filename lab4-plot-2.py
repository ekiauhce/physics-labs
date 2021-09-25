import matplotlib.pyplot as plt

x = [0.1604, 0.1768, 0.1988, 0.2093, 0.2188]
y = [0.3, 0.35, 0.4, 0.45, 0.5]

zero = (0, 0)

slopes = [y[i]/x[i] for i in range(5)]

plt.scatter(x, y, color="none", edgecolor="black")
plt.axline(zero, slope=min(slopes), linestyle="--", color="black")
plt.axline(zero, slope=max(slopes), linestyle="--", color="black")
plt.axline(zero, slope=sum(slopes)/len(slopes), color="black")

plt.show()
