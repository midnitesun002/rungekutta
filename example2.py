# setup virtualenv as needed
# Coded using python3, matplotlib and numpy

import matplotlib.pyplot as plt
import numpy as np

# y' = t * (y - t * sin t)
# y(0) = 1
#
# solution:
# y = t * sin t + cos t

def f(t, y):
    return t * (y - t * np.sin(t))

def RK4(f, y0, t0, tn, h):
    wi = y0
    y = []
    t = [x * h + t0 for x in range(0, 1 + int((tn - t0) / h))]
    for ti in t:
        y.append(wi)
        k1 = h * f(ti, wi)
        k2 = h * f(ti + h/2, wi + k1/2)
        k3 = h * f(ti + h/2, wi + k2/2)
        k4 = h * f(ti + h, wi + k3)
        wi = wi + 1/6*(k1 + 2*k2 + 2*k3 + k4)
    return t, y

def RK45(f, y0, t0, tn, h, e=0.001):
    wi = y0
    ti = start
    y = [wi]
    t = [ti]
    while not ti > stop:
        k1 = h * f(ti, wi)
        k2 = h * f(ti + h/4, wi + k1/4)
        k3 = h * f(ti + 3*h/8, wi + 3*k1/32 + 9*k2/32)
        k4 = h * f(ti + 12*h/13, wi + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
        k5 = h * f(ti + h, wi + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
        k6 = h * f(ti + h/2, wi - 8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 - 11*k5/40)
        wi1 = wi + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5
        wie = wi + 16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55
        R = abs(wie-wi1)/h
        d = 0.84 * (e/R)**(1/4)
        if R <= e:
            wi = wi1
            ti = ti + h
            y.append(wi)
            t.append(ti)
        h = d * h
    return t, y

if __name__ == '__main__':
    start = 0
    stop = 10
    dt = 0.05
    step = 0.0001
    y0 = 1

    # exact
    t1 = np.array([x * dt for x in range(0, int((stop - start) / dt))])
    y1 = t1 * np.sin(t1) + np.cos(t1)

    # RK4
    t2, y2 = RK4(f, y0, start, stop, step)

    # adaptive RK4
    # The following won't stop execution and converge because the RK45
    # algorithm diverges
    #t3, y3 = RK45(f, y0, start, stop, step, e=0.0001)

    plt.plot(t1, y1, 'b-', label='exact')
    plt.plot(t2, y2, 'r:', label='RK4')
    plt.ylim([-6, 8])
    #plt.plot(t3, y3, 'g^', label='RK45')
    plt.legend()
    plt.show()