import matplotlib.pyplot as plt

x = [0.009, 0.023, 0.042, 0.058, 0.062]
y = [0.1, 0.2, 0.3, 0.45, 0.5]
y = [9.8*i for i in y]
zero = (0, 0)

slopes = [y[i]/x[i] for i in range(5)]

plt.scatter(x, y, color="none", edgecolor="black")
plt.axline(zero, slope=min(slopes), linestyle="--", color="black")
plt.axline(zero, slope=max(slopes), linestyle="--", color="black")
plt.axline(zero, slope=sum(slopes)/len(slopes), color="black")

plt.show()
