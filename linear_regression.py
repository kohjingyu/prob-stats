import matplotlib
import matplotlib.pyplot as plt

x = [5, 12, 14, 17, 23, 30, 40, 47, 55, 67, 72, 81, 96, 112, 127]
y = [4, 10, 13, 15, 15, 25, 27, 46, 38, 46, 53, 70, 82, 99, 100]
n = len(x)
assert(n == len(y))

# Plot x and y and save it
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y)
fig.savefig("plot.png")

bar_x = sum(x) / n
bar_y = sum(y) / n

sxy = sum([(x[i] - bar_x) * (y[i] - bar_y) for i in range(n)])
sxx = sum([(x[i] - bar_x)**2 for i in range(n)]) 
syy = sum([(y[i] - bar_y)**2 for i in range(n)]) 

b1 = sxy / sxx
b0 = bar_y - b1 * bar_x

print("\\bar{x} = {0:5f}".format(bar_x))

print("Estimated regression line: y = {0:5f} + {1:5f} x".format(b0, b1))

sse = sum([(y[i] - (b0 + b1 * x[i]))**2 for i in range(n)])
sst = sum([y[i]**2 for i in range(n)]) - sum(y)**2 / n 
sigma_square = sse / (n - 2)

print("SSE: {0:5f}".format(sse))
print("SST: {0:5f}".format(sst))
print("\sigma^2 = {0:5f}".format(sigma_square))
print("\sigma = {0:5f}".format(sigma_square ** 0.5))
print("r^2 = {0:5f}".format(1 - sse / sst))
