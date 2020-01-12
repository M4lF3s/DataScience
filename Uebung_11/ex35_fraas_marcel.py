# Last name(s), First name(s)
# Fraas Marcel

import matplotlib.pyplot as plt
import numpy as np

def f_eval(poly, z):
    """Evaluates a polynomial poly in z"""
    return sum(poly[j]*(z**j) for j in range(len(poly)))

# Setting up parameters
x = np.arange(0.0, 2.75, 0.25)
y = np.asarray([1, 5, 2, 3, 4, 1, 2, 5, 8, 10, 5])


# 1) Create matrices and calculate ATA
n = 3
#m = [(1,2),(3,4),(5,6),(7,8)]
m = list(zip(x,y))

A = [
    [x ** i for i in range(n+1)]
for x,_ in m]

AT = [
    [x ** i for x,_ in m]
for i in range(n+1)]

ATA = [
    [sum(a*b for a,b in zip(row,col)) for col in zip(*A)]
for row in AT]
print(f"ATA = {ATA}")


# 2) Construct vector b
b = [
    [sum(a*b for a,b in zip(row,[y for _,y in m]))]
for row in AT]
print(f"b = {b}")


# 3) solve for a using inverse of ATA dot b
a = [int(value) for value in (np.linalg.inv(ATA)).dot(b)]


# 4) plot data points
plt.scatter(*zip(*m),c='r')

# 5) plot polynomial
x_fine=np.arange(1,10,0.25)
f_x=f_eval(a, x_fine)
plt.plot(f_x)
plt.show()

# 6) n = 3 yields visually best approximation