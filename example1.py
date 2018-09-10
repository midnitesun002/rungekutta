# setup virtualenv as needed
# Coded using python3, matplotlib and numpy

import matplotlib.pyplot as plt
import numpy as np

# y' = y - t^2 + 1
# y(0) = 0.5
#
# solution:
# y = t^2 + 2t + 1 - 1/2e^t

def f(t, y):
    return y - t**2 + 1

start = 0
stop = 4
dt = 0.05
step = 0.5

# exact
t1 = np.array([x * dt for x in range(0, int((stop - start) / dt))])
y1 = t1**2 + 2 * t1 + 1 - 1/2 * np.exp(t1)

# RK4
wi = 0.5
y2 = []
t2 = np.array([x * step for x in range(0, 1 + int((stop - start) / step))])
for ti in t2:
    y2.append(wi)
    k1 = step * f(ti, wi)
    k2 = step * f(ti + step/2, wi + k1/2)
    k3 = step * f(ti + step/2, wi + k2/2)
    k4 = step * f(ti + step, wi + k3)
    wi = wi + 1/6*(k1 + 2*k2 + 2*k3 + k4)

# adaptive RK4
wi = 0.5
ti = 0
y3 = [wi]
t3 = [ti]
e = 0.000001
while not ti > stop:
    k1 = step * f(ti, wi)
    k2 = step * f(ti + step/4, wi + k1/4)
    k3 = step * f(ti + 3*step/8, wi + 3*k1/32 + 9*k2/32)
    k4 = step * f(ti + 12*step/13, wi + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
    k5 = step * f(ti + step, wi + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
    k6 = step * f(ti + step/2, wi - 8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 - 11*k5/40)
    wi1 = wi + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5
    wie = wi + 16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55
    R = abs(wie-wi1)/step
    d = 0.84 * (e/R)**(1/4)
    if R <= e:
        wi = wi1
        ti = ti + step
        y3.append(wi)
        t3.append(ti)
    step = d * step

plt.plot(t1, y1, 'b-', label='exact')
plt.plot(t2, y2, 'r:', label='RK4')
plt.plot(t3, y3, 'g^', label='RK45')
plt.legend()
plt.show()