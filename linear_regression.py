import matplotlib
import matplotlib.pyplot as plt

x = [20, 23, 29, 27, 30, 34, 35, 37, 40, 43]
y = [1.32, 1.67, 2.17, 2.70, 2.75, 2.87, 3.65, 2.86, 3.61, 4.25]
n = len(x)
assert(n == len(y))

# Means
bar_x = sum(x) / n
bar_y = sum(y) / n

# Sum of squares
sxy = sum([(x[i] - bar_x) * (y[i] - bar_y) for i in range(n)])
sxx = sum([(x[i] - bar_x)**2 for i in range(n)]) 
syy = sum([(y[i] - bar_y)**2 for i in range(n)]) 

print("S_xy = {0:5f}, S_xx = {1:5f}, S_yy = {2:5f}".format(sxy ,sxx, syy))

# Point estimates for \beta_0 and \beta_1
b1 = sxy / sxx
b0 = bar_y - b1 * bar_x

print("n = {0}".format(n))
print("\\bar{{x}} = {0:5f}".format(bar_x))
print("\\bar{{y}} = {0:5f}".format(bar_y))

print("Estimated regression line: y = {0:5f} + {1:5f} x".format(b0, b1))

# Plot x and y and save it
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y)
x_values = range(min(x), max(x))
ax.plot(x_values, [b0 + b1 * xi for xi in x_values])
fig.savefig("plot.png")

# error sum of squares
sse = sum([(y[i] - (b0 + b1 * x[i]))**2 for i in range(n)])
# total sum of squares
sst = sum([y[i]**2 for i in range(n)]) - sum(y)**2 / n 
sigma_square = sse / (n - 2)

print("SSE: {0:5f}".format(sse))
print("SST: {0:5f}".format(sst))
print("\sigma^2 = {0:5f}".format(sigma_square))
print("\sigma = {0:5f}".format(sigma_square ** 0.5))
print("r^2 = {0:5f}".format(1 - sse / sst))
